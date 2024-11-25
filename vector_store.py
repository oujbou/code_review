import os
import ssl
import uuid
import shutil
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_utils import extract_zip, is_text_file

load_dotenv()

# MongoDB Atlas connection setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(
    MONGO_URI,
    ssl=True,
    ssl_cert_reqs=ssl.CERT_NONE
)
db = client['github_vector_store']
collection = db['embeddings']

openai_embedding = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))


def store_file_embeddings(zip_path):
    # Generate a unique ID for this project
    project_id = str(uuid.uuid4())

    project_path = extract_zip(zip_path)


    for root, _, files in os.walk(project_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if is_text_file(file_path):
                with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()

                    embedding = openai_embedding.embed_query(content)

                    collection.insert_one({
                        "project_id": project_id,
                        "file_name": file_name,
                        "file_path": file_path,
                        "content": content,
                        "embedding": embedding
                    })

    # Delete the extracted folder of the project after processing
    shutil.rmtree(project_path, ignore_errors=True)
    return project_id

