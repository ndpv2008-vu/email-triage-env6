from pydantic import BaseModel

class Observation(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str
    history: list
    last_action_error: str | None

class Action(BaseModel):
    action: str