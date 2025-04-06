from .base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_sql(self, prompt: str) -> str:
        print(f"[OpenAIClient] Getting SQL for prompt: {prompt}")
        return "SELECT * FROM users;"