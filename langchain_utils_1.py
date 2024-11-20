"""
This file is used if the project to be analysed is not stored in a vector store, but in a folder in the project
files.
"""

import os
from dotenv import load_dotenv
import zipfile
import mimetypes
import openai
from langchain_community.llms import OpenAI
from prompts import get_prompt

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def extract_zip(zip_path, extract_to="extracted_project"):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def is_text_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith("text")

def extract_libraries(project_path):
    libraries = []
    requirements_path = os.path.join(project_path, "requirements.txt")
    if os.path.exists(requirements_path):
        with open(requirements_path, "r") as f:
            libraries = f.read().splitlines()
    return libraries

def extract_config_files(project_path):
    config_contents = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                config_path = os.path.join(root, file)
                with open(config_path, "r") as f:
                    config_contents.append(f.read())
    return config_contents

def extract_code_snippets(project_path):
    code_snippets = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith((".java", ".py", ".ipynb", ".cs", ".PHP",".swift")):
                code_path = os.path.join(root, file)
                with open(code_path, 'r') as f:
                    code_snippets.append(f.read())
    return code_snippets

def analyse_project(zip_path):
    project_path = extract_zip(zip_path)
    libraries = extract_libraries(project_path)
    config_files = extract_config_files(project_path)
    code_snippets = extract_code_snippets(project_path)

    prompt = get_prompt(libraries, config_files, code_snippets)

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user",
             "content": prompt
             }
        ]
    )
    content = response.choices[0].message.content
    return content


