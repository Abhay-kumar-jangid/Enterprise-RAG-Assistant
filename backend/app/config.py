from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOCUMENTS_DIR = os.path.join(BASE_DIR, "data", "documents")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_db")

# Create folders if they don't exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(VECTOR_DB_DIR, exist_ok=True)