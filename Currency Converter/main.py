from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.exampleapi.com/" #base URL Here
API_KEY = " " #Your API_Key Here
printer = PrettyPrinter()

def get_currencies():
    if API_KEY is None:
        print('API Key Not Found! Please Enter an API  Key')
        return None
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url).json()
        if "data" not in response:
            print("Error in Fetching Currency Data")
            return None
        data = list(response['data'].items())
        return data
    except Exception as e:
        print("Something went Wrong:",e)
        return None

def print_currencies(currencies):
    if currencies is None:
        print("Currency Data is Not Available")
    else:
        for currency in currencies:
            name = currency[0]
            print(f"{name}")

def exchange_currency(currencies, from_rate, to_rate, amount):
    rates = dict(currencies)
    if from_rate not in rates or to_rate not in rates:
        print("Invalid Currency Code")
        return
    base_amount = amount / rates[from_rate]
    converted_amount = base_amount * rates[to_rate]
    print(f"{amount} {from_rate} = {round(converted_amount, 2)} {to_rate}")

def main():
    currencies = get_currencies()
    if currencies is None:
        print("Error in loading currency Data")
        return
    print("Welcome to Currency Converter")
    print("List -> Display All Available Currency")
    print("Convert -> From one currency to another currency")
    print("Q -> Quit")
    while True:
        option = input("Enter an Command: ").lower()
        if option == 'q':
            return
        elif option == 'list':
            print_currencies(currencies)
        elif option == 'convert':
            from_rate = input("Enter the Base Currency: ").upper()
            try:
                amount = int(input("Enter the Amount: "))
            except ValueError:
                print('Please Enter a Valid Number')
                continue
            to_rate = input("Enter the Currency to Convert: ").upper()
            exchange_currency(currencies, from_rate, to_rate, amount)
        else:
            print("Unrecognized Operation!")

if __name__ == '__main__':
    main()
