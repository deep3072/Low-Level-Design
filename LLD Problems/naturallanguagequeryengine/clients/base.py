from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def get_sql(self, prompt: str) -> str:
        pass