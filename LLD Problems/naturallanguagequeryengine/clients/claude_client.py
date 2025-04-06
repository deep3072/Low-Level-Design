from .base import LLMClient

class ClaudeClient(LLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_sql(self, prompt: str) -> str:
        print(f"[ClaudeClient] Getting SQL for prompt: {prompt}")
        return "SELECT age FROM users;"
