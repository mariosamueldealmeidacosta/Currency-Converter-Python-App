#imports the necessary libraries for the project
import requests
import json

# Fetch the currency exchange rates from the API
quotation = requests.get("https://api.freecurrencyapi.com/v1/latest?apikey=7qi2PL3RmWTRsa8tMufbnUmtILgfOei45r1kkPqb")
quotation = quotation.json()

# Extract the exchange rates for specific currencies
quotation_euro = quotation['data']['EUR']  
quotation_canada = quotation['data']['CAD']
quotation_china = quotation['data']['CNY']

# Prompt the user to choose a currency for conversion
print("Which currency would you like to convert to? \n Canadian dollar(Type C) \n Euro(Type E) \n Yuan(Type Y)")
currency = input("Type here: ").capitalize().strip()[0]

# Prompt the user for the value to convert
value = int(input("What's the value you want to convert: "))

# Perform the currency conversion based on the chosen currency
if currency == "C":
    dolar_canadian = quotation_canada * value
    print(dolar_canadian)
elif currency == "E":
    dolar_euro = quotation_euro * value
    print(dolar_euro)
elif currency == "Y":
    dolar_yuan = quotation_china * value
    print(dolar_yuan)
else:
    #In case of error the program will show this
    print("There was an error with your request")

