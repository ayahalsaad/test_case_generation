import configparser

config = configparser.ConfigParser()

config.read('config.ini')

OPEN_AI_KEY = config['OPENAI']['OPENAI_API_KEY']
