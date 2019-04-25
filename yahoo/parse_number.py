import re

def parse_content(input):
    
    if input == "-": return 0
    if '/' in input: return input
    if re.search(r'\d', input): return float(float(input.replace(",", ""))) * 1000

    return ""

def numberAmountTostringAmount(input):
    if abs(input) > 1000000000: return "{0:.2f}B".format(input / 1000000000)
    if abs(input) > 1000000: return "{0:.2f}M".format(input / 1000000)
    if abs(input) > 1000: return "{0:.2f}K".format(input / 1000)
    
    return 0
# print(parse_content("5,569,000"))
