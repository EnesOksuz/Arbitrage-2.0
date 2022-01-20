import requests
from win10toast import ToastNotifier
toast = ToastNotifier()

def find(x):
    if((float(x[-1]["price"])-float(x[0]["price"]))>(float(x[-1]["price"])*0.002)):
        print("asdasds")
        toast.show_toast("Arbitrage","Arbitrage was just found",duration=20,icon_path="logo.ico")

def getCoin():
    coins2=[]
    kucoin_cur = "https://api.kucoin.com/api/v1/currencies"
    huobi_cur = "https://api.huobi.pro/v1/common/symbols"
    okex_cur ="https://www.okex.com/api/spot/v3/instruments"
    res_kucoin_cur= requests.get(kucoin_cur).json()
    res_huobi_cur= requests.get(huobi_cur).json()
    res_okex_cur= requests.get(okex_cur).json()
    for x in range(len(res_kucoin_cur["data"])):
        coins2.append(res_kucoin_cur["data"][x]["currency"])
    for x in range(len(res_huobi_cur["data"])):
        coins2.append(res_huobi_cur["data"][x]["base-currency"].upper())
    for x in range(len(res_okex_cur)):
        coins2.append(res_okex_cur[x]["base_currency"])
    coins=list(dict.fromkeys(coins2))

    list_kucoin= res_kucoin_cur["data"]
    list_huobi = res_huobi_cur["data"]
    list_okex = res_okex_cur
    return coins
#hahaha
        
def getPrice(coins):
    
    for x in range(len(coins)):
        data2=[]
        kucoin_price = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level1?symbol="+coins[x]+"-USDT").json()
        huobi_price = requests.get("https://api.huobi.pro/market/detail/merged?symbol="+coins[x].lower()+"usdt").json()
        okex_price = requests.get("https://www.okex.com/api/spot/v3/instruments/"+coins[x]+"-USDT/ticker")
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
         
        
        temp ={}
        
        if(len(data)>1):
            for y in range(len(data)):
                temp[y] = float(data[y]["price"])
            temp = dict(sorted(temp.items(), key=lambda item: item[1]))
            print(temp)
            print("------------------------------------")
            for y in range(len(data)):
                data2.append(data[list(temp.keys())[y]])
            print(data2)
            find(data2)

        


    


        



            
        
#getPrice(getCoin())
print(getPrice((getCoin())))
#def findArbitrage():
   