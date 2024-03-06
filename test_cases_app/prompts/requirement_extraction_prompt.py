from langchain.prompts import PromptTemplate


requirement_extraction_prompt = """
    ROLE:
        As an AI assistant, your task is to meticulously analyze and extract KEY REQUIREMENTS from the provided document that are delimeted with three backticks (```).
        Your goal is to identify and summarize the core functionalities, performance expectations, security measures, and any specific constraints or prerequisites outlined in the document. 
        Pay close attention to details that define what the system or software must do, how it should perform under various conditions, and any standards it must adhere to for security and data protection.

    INSTRUCTIONS:
        1. READ the document thoroughly to understand the context and scope of the project or system being described.
        2. IDENTIFY and list the main functionalities that the system or software is expected to perform. Include any specific features or capabilities that are explicitly mentioned.
        3. EXTRACT performance criteria, including any benchmarks, speed, accuracy, or reliability standards the system must meet.
        4. SUMMARIZE security requirements, focusing on data protection, authentication, authorization, and any other security protocols or standards mentioned.
        5. NOTE any constraints or prerequisites, such as technological dependencies, platform-specific requirements, or compliance with certain regulations or standards.
        6. ORGANIZE the extracted requirements into a clear and concise summary, categorizing them into functionalities, performance criteria, security requirements, and constraints/prerequisites as applicable.

    GOAL:
        By following these instructions, produce a comprehensive summary of the key requirements extracted from the document. This summary should serve as a clear and actionable foundation for further analysis, design, and development activities related to the project or system.
        
        REMEMBER, accuracy and clarity in extracting and summarizing the requirements are crucial for ensuring that the subsequent phases of the project or development process are based on a solid understanding of what needs to be achieved.
        
    IMPORTANT:
        this document is a CHUNKS OF A BRD (Business Requirement Document) and it is a critical part of the project initiation phase. It outlines the business objectives, functional requirements, and constraints of the project. 
        The BRD serves as a reference for all stakeholders involved in the project, including business analysts, developers, testers, and project managers.
        I NEED ACCURATE AND DETAILED REQUIREMENTS EXTRACTED FROM THE DOCUMENT TO ENSURE THAT THE PROJECT IS SUCCESSFULLY INITIATED AND EXECUTED.

        it might include a table of contents, references, or appendices.
        IGNORE ANY TABLE OF CONTENTS, REFERENCES, OR APPENDICES IN THE DOCUMENT. FOCUS ONLY ON THE MAIN BODY OF THE DOCUMENT.

        FOCUS ON FINDING AND EXTRACTING THE REQUIREMENTS IN THE DOCUMENT.

    
    DOCUMENT TO BE ANALYZED:
        document = ```{document}```

      """


def get_requirement_prompt() -> PromptTemplate:
    requirement_prompt = PromptTemplate(
        template=requirement_extraction_prompt, input_variables=["document"]
    )
    return requirement_prompt
