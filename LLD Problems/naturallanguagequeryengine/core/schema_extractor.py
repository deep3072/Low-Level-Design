from core.csv_loader import CSVLoader

class SchemaExtractor:
    def __init__(self, csv_loader: CSVLoader):
        self.csv_loader = csv_loader

    def extract_schema(self) -> str:
        print("[SchemaExtractor] Extracting schema ...")
        return "name TEXT, age INTEGER"