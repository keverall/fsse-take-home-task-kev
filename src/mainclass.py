from fastapi import FastAPI, HTTPException, StaticFiles
import models.request_schemas as request_schemas
import models.response_schemas as response_schemas
import time
import requests
from typing import Dict, List, Tuple

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

BACKEND_URL = "http://127.0.0.1:9000/mock-backend-endpoint"

def validate_client_request(client_request: request_schemas.ClientRequest):
    if not client_request.client_id or not client_request.run_slug:
        raise HTTPException(status_code=400, detail="client_id and run_slug are required")
    if not client_request.observations:
        raise HTTPException(status_code=400, detail="observations are required")
    if not isinstance(client_request.observations, dict):
        raise HTTPException(status_code=400, detail="observations must be a dictionary")
    if not all(isinstance(v, request_schemas.AgentRequest) for v in client_request.observations.values()):
        raise HTTPException(status_code=400, detail="observations must be a dictionary of AgentRequest objects")

def sort_and_group_observations(
    observations: Dict[str, request_schemas.AgentRequest]
) -> Dict[str, List[Tuple[str, request_schemas.AgentRequest]]]:
    sorted_obs = sorted(
        observations.items(),
        key=lambda item: (item[1].nn_model_name, item[1].agent_type or "")
    )
    grouped_requests = {}
    for agent_id, agent_request in sorted_obs:
        model_name = agent_request.nn_model_name
        if model_name not in grouped_requests:
            grouped_requests[model_name] = []
        grouped_requests[model_name].append((agent_id, agent_request))
    return grouped_requests

def get_backend_response(
    backend_url: str, backend_request: request_schemas.BackendRequest
) -> response_schemas.BackendResponse:
    try:
        resp = requests.post(backend_url, json=backend_request.model_dump())
        resp.raise_for_status()
        backend_data = resp.json()
        return response_schemas.BackendResponse(**backend_data)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Backend error: {e}")

def process_client_request(
    client_request: request_schemas.ClientRequest, backend_url: str
) -> response_schemas.ClientResponse:
    start_time = time.time()
    validate_client_request(client_request)
    grouped_requests = sort_and_group_observations(client_request.observations)
    actions = {}

    for model_name, agent_list in grouped_requests.items():
        observation_array = [agent[1].observations for agent in agent_list]
        backend_request = request_schemas.BackendRequest(observation_array=observation_array)
        backend_response = get_backend_response(backend_url, backend_request)
        for (agent_id, _), action in zip(agent_list, backend_response.actions_array):
            actions[agent_id] = response_schemas.AgentResponse(action=action)

    response_time = time.time() - start_time
    return response_schemas.ClientResponse(actions=actions, response_time=response_time)

@app.post("/ClientRequest/", response_model=response_schemas.ClientResponse)
def create_item(clientRequest: request_schemas.ClientRequest):
    return process_client_request(clientRequest, BACKEND_URL)