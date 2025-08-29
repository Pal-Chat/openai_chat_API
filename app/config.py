import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the program's environment
# This allows secure management of sensitive data like API keys and DB URLs
load_dotenv()

# Retrieve the OpenAI API key from environment variables for authentication
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Retrieve the database connection URL from environment variables
# Defaults to a local SQLite database file if not set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
