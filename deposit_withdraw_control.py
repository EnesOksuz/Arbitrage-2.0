from api_key import *
import requests
# Kucoin control
# Huobi control
# Okex control 
# MEXC control
# FTX control
# BYBIT control

def control(subject):
    def kucoin_control(subject):
        kucoin_chains=[]
        chain={}
        control_url =requests.get("https://api.kucoin.com/api/v2/currencies/AVAX").json()
        for x in range(len(control_url["data"]["chains"])):
            chain={}
            chain["chain name"]=control_url["data"]["chains"][x]["chainName"]
            chain["isWithdrawEnabled"]=control_url["data"]["chains"][x][""]
            chain["isDepositEnabled"]=control_url["data"]["chains"][x]["isDepositEnabled"]
            kucoin_chains.append(chain)
        print(kucoin_chains)
    kucoin_control(subject)
        
control("AVAX")
        


