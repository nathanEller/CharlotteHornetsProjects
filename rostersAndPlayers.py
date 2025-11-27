"""
script with all helper functions to return roster and player data. uses basketball reference
https://www.basketball-reference.com/

robots reference
https://www.basketball-reference.com/robots.txt

following are the pip installs
pip install webdriver-manager
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from bs4 import BeautifulSoup

#set request headers
headers = {
	':authority': 'www.basketball-reference.com',
	##':method': 'GET',
	##':path': '/teams/CHO/2026.html',
	##':scheme': 'https',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	'accept-encoding': 'gzip, deflate, br, zstd',
	'accept-language':'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

#return a dataframe of the players on the Hornets for the season ending in year provided
def charlotteRoster(year):
	url=(f'https://www.basketball-reference.com/teams/CHO/{year}.html')

	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	driver.get(url)
	time.sleep(900)
	##table = driver.find_element(By.ID, 'per_game')
	##table_html = table.get_attribute('outerHTML')
	##df = pd.read_html(table_html)[0]
	##print(df.head())
	return 200
