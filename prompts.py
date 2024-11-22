
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

def get_prompt_2(libraries, config_files, code_snippets):
    libraries_text = ", ".join(libraries)
    config_files_text = "\n\n".join(config_files)
    code_snippets_text = "\n\n".join(code_snippets)

    return f"""
    # GitHub Project Analysis

    ## Libraries
    {libraries_text}

    ## Configurations
    {config_files_text}

    ## Code Snippets
    {code_snippets_text}

    Please analyze this project and provide a comprehensive Markdown report that includes the following sections:

    ### 1. General Information
    Provide a high-level summary of the project. Describe its purpose and any notable features or functionalities.

    ### 2. Used Libraries
    - List all libraries used in the project.
    - Explain their purpose and how they are used in the project.

    ### 3. Alternative Libraries or Optimizations
    - Suggest better or more modern alternatives to the libraries used (if applicable).
    - Provide suggestions for optimization related to the libraries.

    ### 4. Configuration Files Analysis and Possible Improvements
    - Analyze the configuration files (YAML, JSON, etc.) and suggest improvements for organization, clarity, or functionality.

    ### 5. Code Analysis
    - Identify any weaknesses in the code, including specific examples of:
      - Security issues
      - Reliability issues
      - Maintainability issues
      - Performance issues
    - Assess the severity of each weakness and provide suggestions for addressing them.
    - Highlight sections of the code where weaknesses occur, if possible.
    - Evaluate the code’s alignment with the ISO 25010 standard for:
      - **Security**
      - **Reliability**
      - **Maintainability**
      - **Performance**

    ### 6. Additional Use Cases
    Suggest additional use cases or extensions for the project that could improve its utility or scope.

    ### Output Instructions
    - The entire report should be formatted in **Markdown**.
    - Use proper Markdown syntax:
      - Headings (`#`, `##`, `###`) for sections.
      - Bullet points (`-`) for lists.
      - Code blocks (```` ``` ````) for code snippets.
    - If a section has no relevant information, state explicitly that there are no findings.

    Ensure that the analysis is detailed, actionable, and professional.
    """

def get_prompt_boss(libraries, config_files, code_snippets):
    libraries_text = ", ".join(libraries)
    config_files_text = "\n\n".join(config_files)
    code_snippets_text = "\n\n".join(code_snippets)

    return f"""
        # GitHub Project Analysis

        ## Libraries
        {libraries_text}

        ## Configurations
        {config_files_text}

        ## Code Snippets
        {code_snippets_text}
        Format d'une fiche de faiblesse

    Créer un fichier markdown nommé [SEVERITE]-[XXX]-[description-courte].md avec la structure suivante :
    
    SEVERITE-XXX] Titre de la faiblesse
    
    ## Information générale
    **Titre**: [Description courte et claire]
    **Sévérité**: [CRITIQUE/ELEVEE/MODEREE/FAIBLE]
    **Occurrences**: [Nombre + localisation]
    **Portée**: [Domaines impactés séparés par /]
    **Catégorie ISO 25010**: [Standards impactés]
    
    ## Description technique
    ### Nature du problème
    [1-2 paragraphes décrivant la problématique]
    
    Les principaux problèmes identifiés sont :
    [Liste des problèmes]
    
    ### Contexte
    [Liste des éléments de contexte importants]
    
    ### Violations
    [Standards/Principes violés]
    
    ## Impact détaillé
    **[Domaine]**: [Impact]
    [Liste des impacts par domaine]
    
    ## Code problématique
    [1-2 paragraphes expliquant les problèmes dans le code]
    
    ```python
    [Code illustrant les problèmes]
    
    ## Solutions possibles
    ### 1. [Nom de la solution] en liste numéroté 
    [1 paragraphe expliquant l'approche]
    pythonCopy[Code de la solution]
    [Répéter pour chaque solution proposée]
    ### Comparaison des solutions
    SolutionAvantagesInconvénientsComplexitéTemps[Solution 1][Liste][Liste][Faible/Moyenne/Élevée][Estimation]
    
    ## Risques associés
    
    [Liste numérotée des risques]
    
    Documentation
    
    Lien 1 : Description
    [Liste des ressources pertinentes avec liens]
    
    Estimation de correction à titre indicatif en heures 
    
    Analyse : Xh
    Développement : Xh
    Tests : Xh
    Documentation : Xh
    Déploiement : Xh
    Total : Xh
    
    Note : Estimation pour un développeur senior. Les IDE modernes (VSCode, PyCharm) facilitent le refactoring 
    automatique, limitant le besoin de connaissance approfondie du code existant.
    """

    
    
