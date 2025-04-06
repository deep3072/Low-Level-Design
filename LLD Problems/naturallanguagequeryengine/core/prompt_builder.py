class PromptBuilder:
    def build_prompt(self, schema: str, question: str) -> str:
        print(f"[PromptBuilder] Building prompt using schema: {schema} and question: {question}")
        return f"Schema: {schema}\nQuestion: {question}"