# Design Natural Language Query Engine

## Requirements

1. The system should allow a user to upload a CSV file containing tabular data.
2. The user can ask a question in natural language based on the contents of the CSV file.
3. The system should convert the natural language question into a valid SQL query using an LLM.
4. The generated SQL query should be executed on the uploaded CSV data.
5. The system should return the results of the SQL query in a structured format.

## Class Diagram
![Class Diagram](https://github.com/user-attachments/assets/e29fc9b7-b6ea-498a-888b-466d22523651)


## Classes, Interfaces, and Enums

1. `CSVLoader`: Responsible for loading the CSV file and creating a temporary SQLite table from it.
2. `SchemaExtractor`: Extracts column names and types from the CSV-loaded table to help build LLM prompts.
3. `PromptBuilder`: Builds the prompt to be sent to the LLM using the table schema and the natural language question.
4. `LLMClient`: Interface that defines the method `get_sql(prompt: str)` which is implemented by all LLM providers.
5. `OpenAIClient`, `GeminiClient`, `ClaudeClient`: Concrete implementations of the `LLMClient` interface, each integrating with its respective provider.
6. `LLMProvider`: Enum that defines the supported LLM providers: `OPENAI`, `GEMINI`, and `CLAUDE`.
7. `LLMClientFactory`: Returns the appropriate `LLMClient` implementation based on the selected `LLMProvider`.
8. `SQLExecutor`: Executes the generated SQL query against the SQLite database and returns the results.
9. `QueryFacade`: Serves as the main orchestrator, managing the complete flow from CSV loading to LLM prompt generation to SQL execution.
10. `Demo`: Demonstrates the usage of the system by creating a mock CSV, initializing the engine, and running a natural language query through the `QueryFacade`.

