from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {
        "state": {
            "email_id": "1",
            "sender": "boss@company.com",
            "subject": "Urgent meeting",
            "body": "Join meeting ASAP",
            "history": [],
            "last_action_error": None
        }
    }

@app.post("/step")
def step(action: dict):
    return {
        "state": {
            "email_id": "1",
            "sender": "boss@company.com",
            "subject": "Urgent meeting",
            "body": "Join meeting ASAP",
            "history": [],
            "last_action_error": None
        },
        "reward": 1,
        "done": False,
        "info": {}
    }