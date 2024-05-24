import requests

response = requests.get("https://coinmarketcap.com/")

response_text = response.text
res_parse_list = []
response_parse = response_text.split("<span>")

for parse_elem_1 in response_parse:
    if(parse_elem_1.startswith('$')):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if (parse_elem_2.startswith("$")) and parse_elem_1[1].isdigit():
                res_parse_list.append(parse_elem_2)


bitcoin_rate = res_parse_list[0]
print("1-*-*-*-*Курс bitcoin---",bitcoin_rate,"*-*-*-*")

ethereum_rate = res_parse_list[1]
print("2-*-*-*-*Курс ethereum--",ethereum_rate," *-*-*-*")

tether_rate = res_parse_list[2]
print("3-*-*-*-*Курс tether----",tether_rate,"-*-*-*-*-*-*")

bnb_rate = res_parse_list[3]
print("4-*-*-*-*Курс bnb-------",bnb_rate,"-*-*-*-*-*")

solana_rate = res_parse_list[4]
print("5-*-*-*-*Курс solana----",solana_rate,"-*-*-*-*-*")

usdc_rate = res_parse_list[5]
print("6-*-*-*-*Курс usdc------",usdc_rate,"-*-*-*-*-*-*")
