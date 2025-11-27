"""
script with all helper functions to return roster and player data. uses basketball reference
https://www.basketball-reference.com/

robots reference
https://www.basketball-reference.com/robots.txt

following are the pip installs
pip install selenium
pip install webdriver-manager
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

#return a dataframe of the players on the Hornets for the season ending in year provided
def charlotteRoster(year):
	url=(f'https://www.basketball-reference.com/teams/CHO/{year}.html')

	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	driver.get(url) #deal with timeouts of js on page

	##page insepction shows that the element to inspect is a table with the id of 'roster'
	table = driver.find_element(By.ID, 'roster')
	outer_html_table = table.get_attribute('outerHTML')
	#time.sleep(15)
	##df = pd.read_html(table_html)[0]
	##print(df.head())
	driver.quit()
	return 200
