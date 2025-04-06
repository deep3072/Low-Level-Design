class CSVLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.table_name = "data"

    def load_csv(self):
        print(f"[CSVLoader] Loading CSV from {self.file_path}")

    def get_connection(self):
        print("[CSVLoader] Returning SQLite connection (mock)")
        return None

    def get_table_name(self) -> str:
        return self.table_name