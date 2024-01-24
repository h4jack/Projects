#a python program to convert currency in real time.
from forex_python.converter import CurrencyRates
c = CurrencyRates()
ccur = {0:"USD",     1:"EUR",     2:"JPY",     3:"BGN",     4:"CZK",     5:"DKK",     6:"GBP",     7:"HUF",      8:"PLN",     9:"RON",
10:"SEK",    11:"CHF",    12:"ISK",    13:"NOK",    14:"TRY",    15:"AUD",     16:"BRL",    17:"CAD",    18:"CNY",    19:"HKD",
20:"IDR",    21:"INR",    22:"KRW",    23:"MXN",     24:"MYR",    25:"NZD",    26:"PHP",    27:"SGD",    28:"THB",    29:"ZAR",}

def main():
    # x = c.get_rates('USD')
    printCCode()
    try:
        a = int(input("Enter Currency key to Convert(e.g. 1 for EUR): "))
        n = float(input("Enter the amount: "))
        b = int(input(f"Convert {n} {ccur[a]} to: "))
    except:
        print("Invalid Input. Try Again...\n")
        main()
        exit()
    print(f"{n} {ccur[a]} is {c.convert(ccur[a], ccur[b], n)} {ccur[b]}")
    
def printCCode():
    print("""Currency with it's Key's:
0. USD,     1. EUR,     2. JPY,     3. BGN,     4. CZK,     5. DKK,     6. GBP,     7. HUF      8. PLN,     9. RON,
10. SEK,    11. CHF,    12. ISK,    13. NOK,    14. TRY,    15. AUD     16. BRL,    17. CAD,    18. CNY,    19. HKD,
20. IDR,    21. INR,    22. KRW,    23. MXN     24. MYR,    25. NZD,    26. PHP,    27. SGD,    28. THB,    29. ZAR,""")


if __name__ == '__main__':
    main()