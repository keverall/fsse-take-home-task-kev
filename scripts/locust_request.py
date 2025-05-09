# ======================================================================================================================
#
# IMPORTS
#
# ======================================================================================================================

import secrets

from locust import HttpUser, between, task
import requests

from src.models.request_schemas import ClientRequest, AgentRequest

# ======================================================================================================================
#
# CLASSES
#
# ======================================================================================================================

class APIUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """This runs when a simulated user starts."""
        self.slug = secrets.randbits(32)

    @task
    def get_data(self):
        """Perform GET request after logging in."""
        schedule_request = ClientRequest(
            client_id="test",
            run_slug=str(self.slug),
            observations={
                "test": AgentRequest(observations=[0.1, 0.2], agent_type="lr", nn_model_name="foundation-v1")
            }
        )

        response = requests.post(
            url="http://0.0.0.0:8080/schedule",
            json=schedule_request.model_dump()
        )

        print(response.json())
