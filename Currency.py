import requests

API_KEY = 'fca_live_xijkcU8fjFFaJhIR0Ol5nGc3uvl2k1769RaORtjQ'
BASE_URL = f"https://app.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "KSH", "TSH", "USH", "RAND", "CNY", "KRW"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
       response = requests.get(url)
       data = response.json(data)
       return data
    except Exception as e:
        print(e)
        return None
    
base = input("Enterthe base currency (e for exit): ").upper()

if base not in CURRENCIES:
    print(Invalid)
 
data = convert_currency("KSH")
for ticker, Value in data.items():
    print(f"{ticker}: {Value}")
