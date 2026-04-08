from models import Observation, Action

class EmailEnv:
    def reset(self):
        return {
            "email_id": "1",
            "sender": "boss@company.com",
            "subject": "Urgent meeting",
            "body": "Join meeting ASAP",
            "history": [],
            "last_action_error": None
        }

    def step(self, action):
        return {
            "state": self.reset(),
            "reward": 1,
            "done": False,
            "info": {}
        }