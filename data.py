from main import *

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = 'https://www.basketball-reference.com/players/a/adamsst01/gamelog/2021/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

headers = [th.getText() for th in soup.findAll('thead', limit=10)[0].findAll('th')]

headers = headers[1:]

# avoid the first header row
rows = soup.findAll('tr')


player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
