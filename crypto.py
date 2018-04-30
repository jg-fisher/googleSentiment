from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import re

overall_sentiment = 0
overall_subjectivity = 0

google_urls = {
	'btc price': 'https://www.google.com/search?q=btc+price&source=lnms&tbm=nws',
	'eth price': 'https://www.google.com/search?q=eth+price&esource=lnms&tbm=nws',
	'ltc price': 'https://www.google.com/search?q=ltc+price&esource=lnms&tbm=nws',
}

response = requests.get(google_urls['eth price'])

soup = BeautifulSoup(response.text, 'html.parser')

headline_results = soup.find_all('div', class_='st')

for text in headline_results:
	blob = TextBlob(text.get_text())	
	overall_sentiment += blob.sentiment.polarity
	overall_subjectivity += blob.sentiment.subjectivity
	print(blob + '\n' + str(blob.sentiment) + '\n' + '\n')

print('Sentiment:', overall_sentiment, 'Subjectivity:', overall_subjectivity)

