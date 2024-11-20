
def get_prompt(libraries, config_files, code_snippets):
    libraries_text = ", ".join(libraries)
    config_files_text = "\n\n".join(config_files)
    code_snippets_text = "\n\n".join(code_snippets)

    return f'''
    f"Project Analysis:\n\n"
    f"Libraries:\n{libraries_text}\n\n"
    f"Configurations:\n{config_files_text}\n\n"
    f"Code:\n{code_snippets_text}\n\n"
    Give ma an extensive report about this Github project.
    Provide a summary of the project, analyze the libraries used and suggest optimizations or alternative libraries,
    analyze the configuration files and suggest improvements, provide optimization suggestions for the code,
    and suggest additional use cases for the code where possible. Do not make things up, if you find no possible
    suggestions or improvement indicate that what you found seems good enough.
    If you cannot find a project, return no project found and don't generate a response
    Use this format:
    ### General informations [2-3 paragraph describing the project]
    ### Used libraries [List the used libraries]
    ### Alternative Libraries or optimisations [Suggest better options for the libraries or optimizations if possible]
    ### Configuration files analysis and possible improvements [brief analysis of the configuration file with possible improvements]
    ### Optimization suggestions for the code [Analysis of the code (show the code snipped) with possible improvements and optimizations, with code examples]
    ### Code weaknesses on a sec
    ### Additional possible use cases for the code
    
    
    '''

def get_prompt_1(libraries, config_files, code_snippets):
    libraries_text = ", ".join(libraries)
    config_files_text = "\n\n".join(config_files)
    code_snippets_text = "\n\n".join(code_snippets)
    return (
        f"Analyze the following Python project and provide a structured JSON response with the sections below. "
        "Do not make assumptions or hallucinate any information. If any section is not relevant or applicable, indicate it explicitly as null.\n\n"

        "### Input Data:\n"
        f"Libraries:\n{libraries_text}\n\n"
        f"Configurations:\n{config_files_text}\n\n"
        f"Code:\n{code_snippets_text}\n\n"

        "### Expected Output Format (in JSON):\n"
        "{\n"
        "  \"general_information\": \"Summary of the project and its purpose in 2-3 paragraphs.\",\n"
        "  \"used_libraries\": \"List of libraries and their purposes in the project.\",\n"
        "  \"alternative_libraries\": \"Suggestions for alternative libraries and possible optimizations.\",\n"
        "  \"configuration_analysis\": \"Analysis of configuration files and any improvements.\",\n"
        "  \"code_optimizations\": \"Suggestions for code optimizations. Show the original code and the suggested improvement\",\n"
        "  \"additional_use_cases\": \"Potential additional use cases for the project.\"\n"
        "}\n\n"

        "### Important:\n"
        "- Follow the JSON structure exactly as shown above.\n"
        "- Do not add any additional information outside the JSON structure.\n"
        "- If a section has no relevant content, use `null` for that section.\n"
    )