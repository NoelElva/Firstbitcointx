#The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
import requests 
# for parsing HTML and XML documents.
from bs4 import BeautifulSoup  
#provides various time-related functions. 
import time
#urllib.error for the exceptions raised.
from urllib.error import HTTPError
C=0 # Condition variable.
A=0 #increment counter.
while C == 0: #loops while the c is equal to zero.
    time.sleep(2.4) #used to add delay.
    B=str(A) #stores A variable in string format.
   
    url="https://www.blockchain.com/explorer/blocks/btc/"+B #URL of the crawling website +B to add the string at the end 
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as hp:
        print(hp)
    else: 
        r = requests.get(url) 
        soup = BeautifulSoup(r.content, 'html.parser')  
        # stores the value of the div with same name and store it in a form of a list
        article_soup = [result.get_text(separator="<div>", strip=True) for result in soup.find_all( 'div', {'class': 'sc-3391354d-2 gOhep'})] 
        print(article_soup)
        #stores the div tag at the 7 index postion 
        rep=article_soup[7]
        if rep != "0.00 BTC"  :
            print ( "first block is :  "+ B )
        
            C=1
        
        else:
            print (A)
            A= A+1
    