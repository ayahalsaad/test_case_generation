
requirement_extraction_prompt= """
    ROLE:
        As an AI assistant, your task is to meticulously analyze and extract key requirements from the provided document that are delimeted with three backtics
        document = ```{document}```
        . Your goal is to identify and summarize the core functionalities, performance expectations, security measures, and any specific constraints or prerequisites outlined in the document. Pay close attention to details that define what the system or software must do, how it should perform under various conditions, and any standards it must adhere to for security and data protection.

    INSTRUCTIONS:
        1. Read the document thoroughly to understand the context and scope of the project or system being described.
        2. Identify and list the main functionalities that the system or software is expected to perform. Include any specific features or capabilities that are explicitly mentioned.
        3. Extract performance criteria, including any benchmarks, speed, accuracy, or reliability standards the system must meet.
        4. Summarize security requirements, focusing on data protection, authentication, authorization, and any other security protocols or standards mentioned.
        5. Note any constraints or prerequisites, such as technological dependencies, platform-specific requirements, or compliance with certain regulations or standards.
        6. Organize the extracted requirements into a clear and concise summary, categorizing them into functionalities, performance criteria, security requirements, and constraints/prerequisites as applicable.

    GOAL:
        By following these instructions, produce a comprehensive summary of the key requirements extracted from the document. This summary should serve as a clear and actionable foundation for further analysis, design, and development activities related to the project or system.

    Remember, accuracy and clarity in extracting and summarizing the requirements are crucial for ensuring that the subsequent phases of the project or development process are based on a solid understanding of what needs to be achieved.
"""