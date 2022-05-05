# Importing Required Libraries
from bs4 import BeautifulSoup
import requests
import pickle

url = 'https://www.bollywoodhungama.com/celebrities/top-100/'

page = requests.get(url).text

soup = BeautifulSoup(page,'lxml')

celeb_title_tag = soup.find_all('h4',class_= 'bh-celeb-title')
celebrities = [ tags.find('a').text for tags in celeb_title_tag ]


pickle.dump(celebrities, open('celebrities_name.pkl','wb'))

