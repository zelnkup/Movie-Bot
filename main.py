import os
import random
import time

from googlesearch import search
from selenium import webdriver

# Show our genres
movies = ['comedy', 'horrors']

print('Choose a genre of movie: ' + str(movies))

# Data of our films
comedy = ['lebowski', 'cyrus', 'date night', 'due date']
horrors = ['bloodshoot', 'the extra man', 'fubar2']

x = input()
if x == 'comedy':
	movie = random.choice(comedy)
elif x == 'horrors':
	movie = random.choice(horrors)
else:
	newmoviews = comedy + horrors
	movie = random.choice(newmoviews)

print('It seems like we will watch ' + movie)

os.system("say 'It seems like we will watch:'" + movie)
time.sleep(20)
os.system("say 'Have a good time!' ")

# Our search query to google
query = ("hdrezka смотреть " + movie)

my_results_list = []

# Scraping first google result
for i in search(query,
				tld='com',
				lang='ru',
				num=1,
				start=0,
				stop=1,
				):
	my_results_list.append(i)

# Open browser page with our film
browser = webdriver.Firefox()
browser.get(my_results_list[0])
