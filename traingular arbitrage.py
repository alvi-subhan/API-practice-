import urllib.parse, requests
from matplotlib import pyplot as plt
import numpy as np

main_url = "https://api.cryptonator.com/api/full/"

print("supported currencies are bitcoin,etherum,litecoin and DogeCoin\n",
      "use btc for bitcoin\n",
      "eth for etherum\n",
      "ltc for litecoin\n",
      "doge for DogeCoin"
      )

currencies = ["btc", "eth", "ltc", "doge"]

while True:
    inp = input("enter your currency ").lower()
    quantity = input("enter quantity of u=your currency")

    try:
        quantity = int(quantity)
    except:
        print("please give numeric input")
        break

    if inp not in currencies:
        print("currency not supported")
        break
    elif inp == "q" or inp == "quit":
        break
    # while x:

    elif inp in currencies:
        currencies.remove(inp)
        print(currencies)
        base = inp
        target = currencies[0]
        another = currencies[1]

        api1 = base + "-" + target
        api2 = target + "-" + another
        api3 = another + "-" + base

        url_api1 = main_url + api1  # url for api1
        url_api2 = main_url + api2
        url_api3 = main_url + api3
        print(url_api1)

        json_api1 = requests.get(url_api1).json()
        print(json_api1)
        json_api2 = requests.get(url_api2).json()
        """json_api3 = requests.get(url_api3).json()

        rate_api1 = int(json_api1["ticker"]["price"])
        print(rate_api1)
        rate_api2 = int(json_api2["ticker"]["price"])
        rate_api3 = int(json_api3["ticker"]["price"])

        if rate_api1 / rate_api2 > rate_api3:
            print("currently there's no opportunity")
        else:
            e1 = quantity * rate_api1
            e2 = e1 * rate_api2
            e3 = e2 * rate_api3

            profit = e3 - quantity

            # jsonn=requests.get("https://api.cryptonator.com/api/full/btc-eth").json()

            # print(jsonn["ticker"])"""

