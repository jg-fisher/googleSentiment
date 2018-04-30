from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import re

class Analysis:
	def __init__(self, term):
		self.term = term
		self.sentiment = 0
		self.subjectivity = 0
		
		self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

	def run(self):
		response = requests.get(self.url)
		
		soup = BeautifulSoup(response.text, 'html.parser')
		
		headline_results = soup.find_all('div', class_='st')
		
		for text in headline_results:
			blob = TextBlob(text.get_text())	
			self.sentiment += blob.sentiment.polarity
			self.subjectivity += blob.sentiment.subjectivity
			print(blob + '\n' + str(blob.sentiment) + '\n' + '\n')
	


a = Analysis('ethereum price')
a.run()
