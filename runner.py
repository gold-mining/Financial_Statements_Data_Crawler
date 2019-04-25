import sys
from tabulate import tabulate

from yahoo.data_income import get_income_data
from yahoo.data_balance import get_balance_data
from yahoo.data_cash_flow import get_cash_flow_data

from output.output import output_file

input = {
    "ticker": "PG", 
    "name": "N/A", 
    "sector": "N/A", 
    "industry": "N/A", 
    "country": "N/A", 
    "market-cap": "N/A"
}

for arg in sys.argv:
    if "=" in arg:
        key, value = arg.split("=")
        input[key] = value

########## 获取数据 ##########
income = get_income_data(input["ticker"])
balance = get_balance_data(input["ticker"])
cash_flow = get_cash_flow_data(input["ticker"])

output_file(input, income, balance, cash_flow)