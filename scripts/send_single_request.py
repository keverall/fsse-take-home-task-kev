# ======================================================================================================================
#
# IMPORTS
#
# ======================================================================================================================

import argparse

import requests

from src.models.request_schemas import ClientRequest, AgentRequest

# ======================================================================================================================
#
# RUN
#
# ======================================================================================================================


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()

    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=str, default="8080")

    # Parse arguments
    args = parser.parse_args()
    schedule_request = ClientRequest(
        client_id="test",
        run_slug=str(0),
        observations={
            "test": AgentRequest(observations=[0.1, 0.2], agent_type="lr", nn_model_name="foundation-v1")
        }
    )

    response = requests.post(
        url=f"http://{args.host}:{args.port}/predict",
        json=schedule_request.model_dump()
    )

    print(response.json())