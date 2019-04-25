def output_file(input, income, balance, cash_flow):
    print("{}: {}".format(input["ticker"], input["name"]))
    print("{:<20}{:<50}{:<30}{:<20}".format(input["sector"], input["industry"], input["country"], input["market-cap"]))
    print(income)
    print(balance)
    print(cash_flow)
    print()