from langchain_openai import AzureOpenAIEmbeddings
from config import (
    AZURE_EMBEDDING_DEPLOYMENT_NAME,
    AZURE_ENDPOINT,
    OPENAI_API_KEY,
)

def get_azure_embeddings() -> AzureOpenAIEmbeddings:
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=AZURE_EMBEDDING_DEPLOYMENT_NAME,
        openai_api_version="2023-09-15-preview",
        api_key=OPENAI_API_KEY,
        azure_endpoint=AZURE_ENDPOINT,
    )
    return embeddings