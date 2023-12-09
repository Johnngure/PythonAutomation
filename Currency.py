import requests

API_KEY = 'fca_live_xijkcU8fjFFaJhIR0Ol5nGc3uvl2k1769RaORtjQ'
BASE_URL = f"https://app.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "KSH", "TSH", "USH", "RAND", "CNY", "KRW"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        
        
    except:
        pass       
