# ======================================================================================================================
#
# IMPORTS
#
# ======================================================================================================================

from pydantic import BaseModel

# ======================================================================================================================
#
# CLASSES
#
# ======================================================================================================================


class BackendRequest(BaseModel):
    observation_array: list[list[float]] = []


class AgentRequest(BaseModel):
    observations: list[float]
    agent_type: str | None
    nn_model_name: str


class ClientRequest(BaseModel):
    client_id: str
    run_slug: str

    observations: dict[str, AgentRequest]
