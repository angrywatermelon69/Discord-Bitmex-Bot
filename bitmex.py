import requests 
import time
import ccxt

#Bitmex base API endpoint
base_url = "https://www.bitmex.com/api/v1"
#-------------------------#

#Function to return recent announcements title and link
def get_announcements():
    #announcements endpoint
    url = base_url + "/announcement?reverse=true" 
    #Initiate API Connection
    r = requests.get(url) 
    #Parse the output to json format
    ann = r.json()
    ann_list = [] #list to hold all dicts returned 
    ann_dict = {} #dict to store key pair values (title, link)

    #loop to store all elements in the dictionary to the list
    for i in ann:
        ann_list.append(i)
    #loop to store all elements in the list to a new filtered dictionary 
    i = 0
    while i < len(ann_list):
        tmp_dict = ann_list[i]
        for j in tmp_dict:
            ann_dict[tmp_dict['title']] = tmp_dict['link'] 
        i = i+ 1
    r.close

    return ann_dict #return (title:link) dictionary

#----------------------------# End of ann function

#Function to return available markets
def markets():
    cli = ccxt.bitmex() #initiate client connection
    mkts = cli.load_markets() #get a raw dict with market data
    av_mkts = [] #string with filtered market data

    for i in mkts:
        tmp_dict = mkts[i]
        for j in tmp_dict:
            if tmp_dict['info']['referenceSymbol'] in av_mkts:
                pass
            else:
                av_mkts.append(tmp_dict['info']['referenceSymbol'])
                
    return av_mkts #Return list with available markets

#-------------------------------------# end of markets function

#Function to return string from last trade of specific Ticker
def last_trade(ticker):
    tickers = ['xbt','ada','bch','eos','eth','ltc','trx','xrp']
    url = "https://www.bitmex.com/api/v1/trade?symbol={}&count=1&reverse=true" 
    if ticker.lower() in tickers:
        url = url.format(ticker)
        r = requests.get(url)
        raw_dict = r.json()
        tmp_string = ''

        for i in raw_dict:
            tmp_dict = i
            tmp_string += 'Symbol: ' + tmp_dict['symbol'] + '\n'
            tmp_string += 'Side: ' + tmp_dict['side'] + '\n'
            tmp_string += 'Price: ' + str(tmp_dict['price'])

        r.close()
        return tmp_string

    else:
        #Execute Loop if input is not valid
        tmp_string = ''
        for i in tickers:
            tmp_string += i.upper() + ' '
        tmp_string = "Ticker not found, please enter one valid ticker: " + tmp_string
        
        return tmp_string
#-----------------------------# end of last trade function

