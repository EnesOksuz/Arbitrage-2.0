import re
import requests
def getCoin():
    coins2=[]
    kucoin_cur = "https://api.kucoin.com/api/v1/currencies"
    huobi_cur = "https://api.huobi.pro/v1/common/symbols"
    okex_cur ="https://www.okex.com/api/spot/v3/instruments"
    mexc_cur ="https://www.mexc.com/open/api/v2/market/symbols"
    bybit_cur ="https://api.bybit.com/v2/public/symbols"
    res_kucoin_cur= requests.get(kucoin_cur).json()
    res_huobi_cur= requests.get(huobi_cur).json()
    res_okex_cur= requests.get(okex_cur).json()
    res_mexc_cur = requests.get(mexc_cur).json()
    res_bybit_cur =requests.get(bybit_cur).json()
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
    coins=list(dict.fromkeys(coins2))
    #coins.sort()
    return coins


def sort(coins):
    for x in range(len(coins)):
        print(coins[x])
        counter =0
        kucoin_control =requests.get(f"https://api.kucoin.com/api/v1/currencies/{coins[x]}")
        huobi_control = requests.get("https://api.huobi.pro/v1/common/currencys")
        okex_control=requests.get("https://www.okex.com/api/spot/v3/instruments")
        mexc_control = requests.get("https://www.mexc.com/open/api/v2/market/symbols")
        
        
    #-------------------FOR KUCOİN---------------------------------------------
        if(kucoin_control.json()["code"]=="200000"):
            counter+=1
    #-----------------FOR HUOBI--------------------------------------------------------
        huobi_coins = huobi_control.json()["data"]
        for y in range(len(huobi_coins)):
            if(coins[x]==huobi_coins[y].upper()):
                counter+=1
    #-----------------FOR OKEX--------------------------------------------------------
        __okex_coins=[]
        for y in range(len(okex_control.json())):
            __okex_coins.append(okex_control.json()[y]["base_currency"])
        okex_coins = list(dict.fromkeys(__okex_coins))
        
        for y in range(len(okex_coins)):
            if(coins[x]==okex_coins[y]):
                counter+=1
     #-----------------FOR MEXC--------------------------------------------------------
        __mexc_coins=[]
        for y in range(len(mexc_control.json()["data"])):
            __mexc_coins.append(mexc_control.json()["data"][y]["vcoinName"])
        mexc_coins= list(dict.fromkeys(__mexc_coins))
        for y in range(len(mexc_coins)):
            if(coins[x]==mexc_coins[y]):
                counter+=1
#API hiz testi yap mexc yavaş çalışıyor
        print(counter)
        
        

sort(getCoin())

