from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.nltk.download('punkt')
from textblob import TextBlob
import re

positive =0
neutral =0
negative =0

def get_full_article(df): # not working currently
    list=[]
    for ind in df.index:
        dict={}
        try:
            article = Article(df['link'][ind],config=config)
            article.download()
            article.parse()
            article.nlp()
        except:
            article = Article(df['link'][ind],config=config)
            article.download('punkt')
            article.parse()
            article.nlp()
        dict['Date']=df['date'][ind]
        dict['Media']=df['media'][ind]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        list.append(dict)
        print(dict)
    news_df=pd.DataFrame(list)

def calculate_percentage():
    total = positive+negative+neutral
    posi_percent = positive/total
    print("Positive Sentiment: "+str(posi_percent*100))
    # nuet_percent = neutral/total
    # print("Neutral Sentiment "+ str(nuet_percent*100))
    nega_percent = negative/total
    print("Negative Sentiment "+str(nega_percent*100))

def clean_text(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyse_text(tweet):
    analysis = TextBlob(clean_text(tweet))
    if analysis.sentiment.polarity >0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

# news_df.to_excel("articles.xlsx")

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agentgooglenews=GoogleNews(start='05/01/2020',end='05/31/2020')
googlenews = GoogleNews()
googlenews.search('Bitcoin')
# result=googlenews.result(sort=True)
result=googlenews.get_texts()
for i in result:
    sentiment = analyse_text(i)
    # print(i)
    if sentiment ==1:
        positive= positive+1
    elif sentiment==0:
        neutral = neutral+1
    else:
        negative = negative +1
    calculate_percentage()
df=pd.DataFrame(result)
# print(df.head())
for i in range(2,20):
    googlenews.getpage(i)
    # result=googlenews.result(sort=True)
    result = googlenews.get_texts()
    for x in result:
        sentiment = analyse_text(x)
        # print(i)
        if sentiment ==1:
            positive= positive+1
        elif sentiment==0:
            neutral = neutral+1
        else:
            negative = negative +1
        calculate_percentage()
    df=pd.DataFrame(result)
    # print(type(df['title']))
    # sentiment = analyse_text(str(df['title']))
    # global positive, negative, neutral
    
    # calculate_percentage()