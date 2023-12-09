import requests

API_KEY = ''
BASE_URL = f"={API_KEY}"

CURRENCIES = ["USD", "EUR", "KSH", "TSH", "USH", "RAND"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    
