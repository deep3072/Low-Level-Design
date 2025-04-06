from core.query_facade import QueryFacade
from clients.factory import LLMClientFactory
from enums.llm_provider import LLMProvider
import pandas as pd

class Demo:
    """
    Simulating the implementation of Natural language to SQL to output engine.
    """
    def create_csv(file_path):
        data = {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [31, 25, 35],
            "city": ["NY", "LA", "Chicago"]
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        print(f"[Demo] CSV created at {file_path}")

    @staticmethod
    def run():
        
        csv_path = "users.csv"
        Demo.create_csv(csv_path)

        provider = LLMProvider.GEMINI
        api_key = "some-api-key"
        llm_client = LLMClientFactory.get_client(provider, api_key)

        facade = QueryFacade(llm_client)
        question = "Show all users older than 30" # question by user
        result = facade.run(csv_path, question)

        print("\n ---- Final Output ---- ")
        for row in result:
            print(row)

if __name__ == "__main__":
    Demo.run()
