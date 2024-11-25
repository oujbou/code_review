import os
from dotenv import load_dotenv
import zipfile
import mimetypes
import openai
from langchain_community.llms import OpenAI
from pymongo import MongoClient

from prompts import get_prompt_boss_2

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

MONGO_URI = os.getenv("MONGO_URI")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["github_vector_store"]
embeddings_collection = db["embeddings"]

def extract_zip(zip_path, extract_to="extracted_project"):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def is_text_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith("text")

def retrieve_project_files(project_id):
    return list(embeddings_collection.find({"project_id":project_id}))

def analyse_project_from_store(project_id):

    project_files = retrieve_project_files(project_id)

    libraries = []
    config_files = []
    code_snippets = []

    for file in project_files:
        file_name = file["file_name"]
        content = file["content"]

        if file_name.endswith("requirements.txt"):
            libraries.extend(content.splitlines())
        elif file_name.endswith((".yaml", ".yml")):
            config_files.append(content)
        elif file_name.endswith((".java", ".py", ".ipynb", ".cs", ".php", ".swift")):
            code_snippets.append(content)

    prompt = get_prompt_boss_2(libraries, config_files, code_snippets)

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user",
             "content": prompt
             }
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    return content





