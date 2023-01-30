import requests
from bs4 import BeautifulSoup
import pandas as pd

#Variablen
excel_name = 'Urheber und Reihen.xlsx'
username = input('Username: ')
password = input('Password: ')

url = 'https://www.buchzentrum.ch/de/landingpage'
url_novitaeten = 'https://www.buchzentrum.ch/de/buecher/novitaeten/novitaeten-belletristik'

# Datensatz einlesen
excel = pd.read_excel(excel_name)
df = pd.DataFrame(excel)
print('einzigartige Autoren:', len(df['1. Urheber'].unique()), 'einzigartige Buchserien:', len(df['Alle Reihen'].unique()))

# webscraper
test = 'https://richterich-ag.ch/'

# page with payloada
'''payload = {'inUserName': username, 'inPassword': password}
page = requests.post(test, data = payload)'''

page = requests.get(test)
print('Serverstatus:', requests.get(test).status_code)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# othmar Richterich
lists = soup.find_all('h2', class_ = 'elementor-heading-title elementor-size-default')
print('Ausgabe von Othmar Richterich:', lists[1].text)


