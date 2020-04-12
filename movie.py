# Import library for web 
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 

# Main Function for scraping 
def main(emotion): 
 
	# movie against emotion Sad 
	if(emotion == "Sad"): 
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Disgust 
	elif(emotion == "Disgust"): 
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Anger 
	elif(emotion == "Anger"): 
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Anticipation 
	elif(emotion == "Anticipation"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Fear 
	elif(emotion == "Fear"): 
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Enjoyment 
	elif(emotion == "Enjoyment"): 
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
 
	# movie against emotion Trust 
	elif(emotion == "Trust"): 
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	# movie against emotion Surprise 
	elif(emotion == "Surprise"): 
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

	response = HTTP.get(urlhere) 
	data = response.text 

	soup = SOUP(data, "lxml") 

	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
	return title 
 
if __name__ == '__main__': 

	emotion = input("Enter the emotion: ") 
	a = main(emotion) 
	count = 0

	for i in a: 
			tmp = str(i).split('>') 

			if(len(tmp) == 3): 
				print(tmp[1][:-3]) 

			if(count > 11): 
				break
			count+=1
