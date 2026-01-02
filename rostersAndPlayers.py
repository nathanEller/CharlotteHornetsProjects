"""
script with all helper functions to return roster and player data. uses basketball reference
https://www.basketball-reference.com/

robots reference
https://www.basketball-reference.com/robots.txt

following are the pip installs
pip install selenium
pip install pandas
"""
from selenium import webdriver
from selenium.webdriver.common.by import By 
from io import StringIO
from bs4 import BeautifulSoup
import pandas as pd
import time

"""
take a player name and return their idTag
player name will be passed as FirstName LastName (with space)
Format: (last initial)/(first 5 letters of last name)(first 2 letters of first name)(01, 02, etc.).
"""
def playerNameToID(playerName):
	firstLast = playerName.lower().split() #returns a list of two strings, the first name followed by the last name
	lastInitial = (firstLast[1])[0]

	if len(firstLast[1]) < 5:
		lastNameLetters = firstLast[1]
	else:
		lastNameLetters = firstLast[1][:5]

	if len(firstLast[0]) < 2:
		firstNameLetters = firstLast[0]
	else:
		firstNameLetters = firstLast[0][:2]
	idTag=(f'{lastInitial}/{lastNameLetters}{firstNameLetters}01')#need to determine when 01 vs 02
	return idTag

"""
return a dataframe of the players on the Hornets for the season ending in year provided
"""
def getRoster(year):
	#give url and instruct selenium to have eager loading to prevent timeout errors
	url = (f'https://www.basketball-reference.com/teams/CHO/{year}.html')
	options = webdriver.ChromeOptions()
	options.page_load_strategy = 'eager'

	#instantiate driver and make connection; sleeping 2 seconds to give elements time to load
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	time.sleep(2)

	#get beautiful soup object
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')

	#page insepction shows that the element to inspect is a table with the id of 'roster'
	table = soup.find(id = 'roster')

	# extracting records from table
	all_trs = table.find_all('tr')
	data_rows = all_trs[1:] #first table row is a header row

	#return the players basketball reference player tag
	links = []
	for i,row in enumerate(data_rows):
		first_href = row.find('a')
		if first_href:
			links.append(first_href.get('href'))

	#get the player name and info
	df = []
	df = pd.read_html(StringIO(str(table)))[0]

	df['playerTag'] = links
	driver.quit()
	return df
	
"""
return dataframe of player counting stats or player advanced stats for their career
mode will be either "count" or "advanced"
"""
def getPlayerStats(player, mode):

	idTag = playerNameToID(player)
	url = (f'https://www.basketball-reference.com/players/{idTag}.html')

	#options to avoid timeouts in loading the webpage
	options = webdriver.ChromeOptions()
	options.page_load_strategy = 'eager'

	#instantiate driver and make connection; sleeping 2 seconds to give elements time to load
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	time.sleep(2)

	if(mode == 'count'):
		
		table = driver.find_element(By.ID, 'totals_stats') #id of element of table for traditional counting stats
		table_html = table.get_attribute('outerHTML')
		df = pd.read_html(StringIO(table_html))[0]
		driver.quit()

	elif(mode == 'adv'):

		table = driver.find_element(By.ID, 'advanced') #id of element of table for traditional counting stats
		table_html = table.get_attribute('outerHTML')
		df = pd.read_html(StringIO(table_html))[0]
		driver.quit()

	else:
		print("i am in the else block")

	return df

"""
returs a dataframe of a player's game logs from a given year
"""
def getGameLog(player, Year):
	idTag = playerNameToID(player)
	url =(f'https://www.basketball-reference.com/players/{idTag}/gamelog/{Year}') #no html in this url

	#options to avoid timeouts in loading the webpage
	options = webdriver.ChromeOptions()
	options.page_load_strategy = 'eager'

	#instantiate driver and make connection; sleeping 2 seconds to give elements time to load
	driver = webdriver.Chrome(options=options)
	driver.get(url)
	time.sleep(2)

	#page insepction shows that the element to inspect is a table with the id of 'player_game_log_reg'
	table = driver.find_element(By.ID, 'player_game_log_reg')
	table_html = table.get_attribute('outerHTML')
	df = pd.read_html(StringIO(table_html))[0]

	#clean up connection
	driver.quit()

	return df