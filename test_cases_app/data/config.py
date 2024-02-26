import configparser

config = configparser.ConfigParser()

config.read('config.ini')

OPENAI_API_KEY = config['AZURE_LANGCHAIN_OPENAI']['AZURE_OPENAI_API_KEY']
AZURE_ENDPOINT = config['AZURE_LANGCHAIN_OPENAI']['AZURE_OPENAI_ENDPOINT']
