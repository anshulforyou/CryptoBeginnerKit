# CryptoBeginnerKit
 
This repo contains the necessary code for anyone who are interested in crypto currency and wants to analyse that news affect the crypto price.

The file news_analysis.py contains the code to fetch all the headlines and article from google news regarding the keyword which we mention in the code. Then we use textblob to do sentiment analysis over all the text that we got.

The bitcoin.py file contains the code to track the bitcoin price using the coinmarketcap API, here we can set a limit that at what current price do we want to trigger alert. Apart from the alert, we are also getting the latest price every five minutes in our telegram account. For implementing the notifications and alert, I have used IFTTT. 