
from bs4 import BeautifulSoup
import pandas as pd

with open ('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify())

# Create Dictionary 
sn_tweets ={}
tweets_no = 0

for texts in soup.find_all('div', class_="tweets-card"):
    tweets = texts.p.text
    tweets_no +=1
    sn_tweets[tweets_no] = [tweets]


sn_tweets_df = pd.DataFrame.from_dict(sn_tweets, orient ='index', columns = ['Tweets'])
print(sn_tweets_df.head())

sn_tweets_df.to_csv('tweets.csv')
print(tweets_no)

