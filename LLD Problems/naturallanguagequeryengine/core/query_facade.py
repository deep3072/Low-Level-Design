from core.csv_loader import CSVLoader
from core.schema_extractor import SchemaExtractor
from core.prompt_builder import PromptBuilder
from core.sql_executor import SQLExecutor
from clients.base import LLMClient

class QueryFacade:
    def __init__(self, llm_client: LLMClient):
        self.csv_loader = None
        self.schema_extractor = None
        self.prompt_builder = PromptBuilder()
        self.sql_executor = None
        self.llm_client = llm_client

    def run(self, csv_path: str, question: str):
        print(f"[QueryFacade] Running query for question: {question}")
        
        self.csv_loader = CSVLoader(csv_path)
        self.csv_loader.load_csv()

        self.schema_extractor = SchemaExtractor(self.csv_loader)
        schema = self.schema_extractor.extract_schema()

        prompt = self.prompt_builder.build_prompt(schema, question)
        sql = self.llm_client.get_sql(prompt)

        self.sql_executor = SQLExecutor(self.csv_loader)
        result = self.sql_executor.execute(sql)

        print("[QueryFacade] Final result:")
        print(result)
        return result
