import string
import pandas as pd
import requests
from bs4 import BeautifulSoup
from main import playersDic, get_key
from nameMaker import nameCreator


for i in sorted(playersDic.values(), reverse=True):
    name, first = nameCreator(
        get_key(i).__getattribute__('name').lower().translate(str.maketrans('', '', string.punctuation)))
    print(name, first)


URL = 'https://www.basketball-reference.com/players/h/hardeja01/gamelog/2021'
page = requests.get(URL)



soup = BeautifulSoup(page.content, 'html.parser')

headers = [th.getText() for th in soup.findAll('thead', limit=10)[0].findAll('th')]

headers = headers[1:]


rows = soup.findAll('tr')

player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]



stats = pd.DataFrame(player_stats, columns=headers)

print(stats)

