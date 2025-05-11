""" description: FastAPI server for handling requests from the client 
    and forwarding them to the backend.
author: Kev Everall """

import time

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from .models.request_schemas import BackendRequest, AgentRequest, ClientRequest
from .models.response_schemas import BackendResponse, AgentResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/ClientRequest/")
async def create_item(clientRequest: ClientRequest):
    """ description: ClientRequest endpoint for handling requests from the client
        author: Kev Everall """
    start_time = time.time()

    # Validation (as before)
    if not clientRequest.client_id or not clientRequest.run_slug:
        raise HTTPException(
            status_code=400, detail="client_id and run_slug are required"
        )
    if not clientRequest.observations:
        raise HTTPException(status_code=400, detail="observations are required")
    if not isinstance(clientRequest.observations, dict):
        raise HTTPException(status_code=400, detail="observations must be a dictionary")
    if not all(
        isinstance(v, AgentRequest)
        for v in clientRequest.observations.values()
    ):
        raise HTTPException(
            status_code=400,
            detail="observations must be a dictionary of AgentRequest objects",
        )

    # Sort observations by nn_model_name and agent_type
    sorted_obs = sorted(
        clientRequest.observations.items(),
        key=lambda item: (item[1].nn_model_name, item[1].agent_type or ""),
    )

    # Group AgentRequest objects by nn_model_name
    grouped_requests = {}
    for agent_id, agent_request in sorted_obs:
        model_name = agent_request.nn_model_name
        if model_name not in grouped_requests:
            grouped_requests[model_name] = []
        grouped_requests[model_name].append((agent_id, agent_request))

    actions = {}

    # For each group, send BackendRequest and map BackendResponse to AgentResponse
    async with httpx.AsyncClient() as client:
        for model_name, agent_list in grouped_requests.items():
            observation_array = [agent[1].observations for agent in agent_list]
            backend_request = BackendRequest(
                observation_array=observation_array
            )

            backend_url = "http://127.0.0.1:9000/mock-backend-endpoint"
            try:
                backend_resp = await client.post(
                    backend_url, json=backend_request.model_dump()
                )
                backend_resp.raise_for_status()
                backend_data = backend_resp.json()
                backend_response = BackendResponse(**backend_data)
            except Exception as e:
                raise HTTPException(
                    status_code=502, detail=f"Backend error for model {model_name}: {e}"
                )

            for (agent_id, _), action in zip(
                agent_list, backend_response.actions_array
            ):
                actions[agent_id] = AgentResponse(action=action)

    response_time = time.time() - start_time

    # Return actions grouped by client_id
    return {
        clientRequest.client_id: {
            "actions": {k: v.dict() for k, v in actions.items()},
            "response_time": response_time,
        }
    }
