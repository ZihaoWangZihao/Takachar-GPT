import os
from dotenv import load_dotenv

def load_api_keys():
    load_dotenv()
load_api_keys()
os.getenv("API_KEY")