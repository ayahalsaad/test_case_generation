from langchain_openai import AzureOpenAIEmbeddings
from config import (
    AZURE_EMBEDDING_DEPLOYMENT_NAME,
    EMBEDDING_ENDPOINT,
    EMBEDDING_API_KEY,
)


def get_azure_embeddings() -> AzureOpenAIEmbeddings:
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=AZURE_EMBEDDING_DEPLOYMENT_NAME,
        openai_api_version="2023-09-15-preview",
        api_key=EMBEDDING_API_KEY,
        azure_endpoint=EMBEDDING_ENDPOINT,
    )
    return embeddings
