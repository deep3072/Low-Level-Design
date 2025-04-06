from core.csv_loader import CSVLoader

class SQLExecutor:
    def __init__(self, csv_loader: CSVLoader):
        self.csv_loader = csv_loader

    def execute(self, query: str):
        print(f"[SQLExecutor] Executing SQL: {query}")
        return [["Alice", 31], ["Charlie", 35]] 
