from tkinter import E
import requests
import time
def getCoin():
    coins2=[]
    sortedcoins=[]
    kucoin_cur = requests.get("https://api.kucoin.com/api/v1/currencies")
    kucoin_coins=[]
    for y in range(len(kucoin_cur.json()["data"])):
        kucoin_coins.append(kucoin_cur.json()["data"][y]["currency"])
    
    huobi_cur = requests.get("https://api.huobi.pro/v1/common/currencys")
    huobi_coins = huobi_cur.json()["data"]
    
    okex_cur =requests.get("https://www.okex.com/api/spot/v3/instruments")
    __okex_coins=[]
    for y in range(len(okex_cur.json())):
        __okex_coins.append(okex_cur.json()[y]["base_currency"])
    okex_coins = list(dict.fromkeys(__okex_coins))

    mexc_cur =requests.get("https://www.mexc.com/open/api/v2/market/symbols")
    __mexc_coins=[]
    for y in range(len(mexc_cur.json()["data"])):
        __mexc_coins.append(mexc_cur.json()["data"][y]["vcoinName"])
    mexc_coins= list(dict.fromkeys(__mexc_coins))

    ftx_cur = requests.get("https://ftx.com/api/wallet/coins")
    ftx_coins=[]
    for y in range(len(ftx_cur.json()["result"])):
        ftx_coins.append(ftx_cur.json()["result"][y]["id"])

    bybit_cur =requests.get("https://api.bybit.com/v2/public/symbols")
    bybit_coins=[]
    for y in range(len(bybit_cur.json()["result"])):
        bybit_coins.append(bybit_cur.json()["result"][y]["base_currency"])

    coins2= kucoin_coins+ huobi_coins+okex_coins+ mexc_coins+ ftx_coins + bybit_coins

    coins=list(dict.fromkeys(coins2))
    for x in range(len(coins)):
    
        counter=0
        for y in range(len(kucoin_coins)):
            if(coins[x]==kucoin_coins[y]):
                counter+=1
        for y in range(len(huobi_coins)):
            if(coins[x]==huobi_coins[y].upper()):
                counter+=1
        for y in range(len(okex_coins)):
            if(coins[x]==okex_coins[y]):
                counter+=1
        for y in range(len(mexc_coins)):
            if(coins[x]==mexc_coins[y]):
                counter+=1
        for y in range(len(ftx_coins)):
            if(coins[x]==ftx_coins[y]):
                counter+=1
        for y in range(len(bybit_coins)):
            if(coins[x]==bybit_coins[y]):
                counter+=1
        if(counter>1):
            sortedcoins.append(coins[x])
    sortedcoins.sort()
    trash =[]
    for x in range(len(sortedcoins)):
        if(sortedcoins[x].find("3S")!=-1 or sortedcoins[x].find("3L")!=-1 or sortedcoins[x].find("2L")!=-1 or sortedcoins[x].find("2S")!=-1):
            trash.append(sortedcoins[x])
            print(sortedcoins[x])
    for x in range(len(trash)):
        sortedcoins.remove(trash[x])
    print(sortedcoins)

    return sortedcoins
        
        

getCoin()       
        
    
    
