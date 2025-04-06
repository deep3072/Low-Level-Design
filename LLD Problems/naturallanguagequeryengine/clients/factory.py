from .openai_client import OpenAIClient
from .gemini_client import GeminiClient
from .claude_client import ClaudeClient
from .base import LLMClient
from enums.llm_provider import LLMProvider

class LLMClientFactory:
    @staticmethod
    def get_client(provider: LLMProvider, api_key: str) -> LLMClient:
        print(f"[Factory] Getting client for: {provider}")
        if provider == LLMProvider.OPENAI:
            return OpenAIClient(api_key)
        elif provider == LLMProvider.GEMINI:
            return GeminiClient(api_key)
        elif provider == LLMProvider.CLAUDE:
            return ClaudeClient(api_key)
        else:
            raise ValueError("Unsupported provider")