import streamlit as st
from vector_store import store_file_embeddings
from langchain_utils import analyse_project_from_store
import os


st.title("Project Analyzer")
st.write("Upload a ZIP file of your project to start the analysis")

uploaded_file = st.file_uploader("Upload your project ZIP file", type=["zip"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    zip_path = f"temp/{uploaded_file.name}"
    os.makedirs("temp", exist_ok=True)
    with open(zip_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    # Store the project in the vector store
    st.info("Processing the project ...")
    try:
        project_id = store_file_embeddings(zip_path)
        st.success(f"Project store in vector store with ID: {project_id}")
    except Exception as e:
        st.error(f"Failed to store in vector store: {e}")
        st.stop()

    # Analyse the project
    st.info("Analysing the project ...")
    try:
        markdown_report = analyse_project_from_store(project_id)
        st.success("Analysis completed")

        st.markdown(markdown_report)

        markdown_path = f"temp/{project_id}_report.md"
        with open(markdown_path, "w") as f:
            f.write(markdown_report)

        with open(markdown_path, "rb") as md_file:
            st.download_button(
                label="Download Markdown Report",
                data=md_file,
                file_name=f"{project_id}_report.md",
                mime="text/markdown",
            )
    except Exception as e:
        st.error(f"Failed to analyse the project:{e}")
