import requests
from win10toast import ToastNotifier
toast = ToastNotifier()

def find(x):
    if((float(x[-1]["price"])-float(x[0]["price"]))>(float(x[-1]["price"])*0.05)):
        print("asdasds")
        toast.show_toast("Arbitrage","Arbitrage was just found",duration=20,icon_path="logo.ico")

def getCoin():
    coins2=[]
    kucoin_cur = "https://api.kucoin.com/api/v1/currencies"
    huobi_cur = "https://api.huobi.pro/v1/common/symbols"
    okex_cur ="https://www.okex.com/api/spot/v3/instruments"
    mexc_cur ="https://www.mexc.com/open/api/v2/market/symbols"
    bybit_cur ="https://api.bybit.com/v2/public/symbols"
    cro_cur ="https://api.crypto.com/v2/public/get-instruments"
    res_kucoin_cur= requests.get(kucoin_cur).json()
    res_huobi_cur= requests.get(huobi_cur).json()
    res_okex_cur= requests.get(okex_cur).json()
    res_mexc_cur = requests.get(mexc_cur).json()
    res_bybit_cur =requests.get(bybit_cur).json()
    res_cro_cur = requests.get(cro_cur).json()
    for x in range(len(res_kucoin_cur["data"])):
        coins2.append(res_kucoin_cur["data"][x]["currency"])
    for x in range(len(res_huobi_cur["data"])):
        coins2.append(res_huobi_cur["data"][x]["base-currency"].upper())
    for x in range(len(res_okex_cur)):
        coins2.append(res_okex_cur[x]["base_currency"])
    for x in range(len(res_mexc_cur["data"])):
        coins2.append(res_mexc_cur["data"][x]["vcoinName"])
    for x in range (len(res_bybit_cur["result"])):
        coins2.append(res_bybit_cur["result"][x]["base_currency"])
    for x in range(len(res_cro_cur["result"]["instruments"])):
        coins2.append(res_cro_cur["result"]["instruments"][x]["quote_currency"])
    coins=list(dict.fromkeys(coins2))

    list_kucoin= res_kucoin_cur["data"]
    list_huobi = res_huobi_cur["data"]
    list_okex = res_okex_cur
    return coins
        
def getPrice(coins):
    
    for x in range(len(coins)):
        data2=[]
        kucoin_price = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level1?symbol="+coins[x]+"-USDT").json()
        huobi_price = requests.get("https://api.huobi.pro/market/detail/merged?symbol="+coins[x].lower()+"usdt").json()
        okex_price = requests.get("https://www.okex.com/api/spot/v3/instruments/"+coins[x]+"-USDT/ticker")
        mexc_price =requests.get("https://www.mexc.com/open/api/v2/market/ticker?symbol="+ coins[x].lower()+"_usdt")
        ftx_price = requests.get(f"https://ftx.com/api/markets/{coins[x]}/usdt/orderbook?depth=1")
        bybit_price= requests.get(f"https://api.bybit.com/v2/public/tickers?symbol={coins[x]}USDT")
        cro_price = requests.get(f"https://api.crypto.com/v2/public/get-ticker?instrument_name={coins[x]}_USDT").json()
        data =[]

        print(coins[x])
        if(kucoin_price["data"]):
            dictt={}
            dictt["exchange"]="kucoin"
            dictt["price"]=kucoin_price["data"]["price"]
            dictt["link"]=f"https://trade.kucoin.com/trade/{coins[x].lower()}-USDT"
            data.append(dictt)
            
        if(huobi_price["status"]=="ok"):
            dictt={}
            dictt["exchange"]="huobi"
            dictt["price"]=huobi_price["tick"]["bid"][0]
            dictt["link"]=f"https://www.huobi.com/en-us/exchange/{coins[x].lower()}_usdt"
            data.append(dictt)
         
        if(okex_price.status_code==200):
            dictt={}
            dictt["exchange"]="okex"
            dictt["price"]=okex_price.json()["best_ask"]
            dictt["link"]=f"https://www.okex.com/tr/trade-spot/{coins[x].lower()}-usdt"
            data.append(dictt)
        if(mexc_price.status_code==200):
            dictt={}
            dictt["exchange"]="mexc"
            dictt["price"]=mexc_price.json()["data"][0]["last"]
            dictt["link"]=f"https://www.mexc.com/tr-TR/exchange/{coins[x]}_USDT"         
            data.append(dictt)
        if(ftx_price.status_code==200):
            dictt={}
            dictt["exchange"]="ftx"
            dictt["price"]=ftx_price.json()["result"]["bids"][0][0]
            dictt["link"]=f"https://ftx.com/trade/{coins[x]}/USDT"
            data.append(dictt)
        if(bybit_price.json()["ret_msg"]=="OK"):
            dictt={}
            dictt["exchange"]="bybit"
            dictt["price"]=bybit_price.json()["result"][0]["last_price"]
            dictt["link"]=f"https://www.bybit.com/en-US/trade/spot/{coins[x]}/USDT"
            data.append(dictt)
        if(type(cro_price["result"]["data"])==type({})):
            dictt={}
            dictt["exchange"]="cro"
            dictt["price"]=cro_price["result"]["data"]["a"]
            dictt["link"]=f"https://api.crypto.com/v2/public/get-ticker?instrument_name={coins[x]}_USDT"
            data.append(dictt)


            
        temp ={}
        print(data)
        
        # if(len(data)>1):
        #     for y in range(len(data)):
        #         temp[y] = float(data[y]["price"])
        #     temp = dict(sorted(temp.items(), key=lambda item: item[1]))
        #     print(temp)
        #     print("------------------------------------")
        #     for y in range(len(data)):
        #         data2.append(data[list(temp.keys())[y]])
        #     print(data2)
        #     find(data2)

        


    


        



            
        
#getPrice(getCoin())
print(getPrice((getCoin())))
#def findArbitrage():
   