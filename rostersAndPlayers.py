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
import pandas as pd
import time

#return a dataframe of the players on the Hornets for the season ending in year provided
def charlotteRoster(year):
	#give url and instruct selenium to have eager loading
	url=(f'https://www.basketball-reference.com/teams/CHO/{year}.html')
	options= webdriver.ChromeOptions()
	options.page_load_strategy = 'eager'

	#instantiate driver and make connection
	driver=webdriver.Chrome(options=options)
	driver.get(url) 

	##5 seconds to give basic html elements time to load
	time.sleep(2)

	##page insepction shows that the element to inspect is a table with the id of 'roster'
	table = driver.find_element(By.ID, 'roster')
	table_html = table.get_attribute('outerHTML')
	
	df = pd.read_html(table_html)[0]

	#clean up connection
	driver.quit()
	return df

#return player stats for a given year
def playerStatsYear(playerName, year):
	return 200