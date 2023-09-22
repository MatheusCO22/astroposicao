from bs4 import BeautifulSoup
import requests
import pandas as pd

with open('./catalog.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

table = soup.find('table', class_='brightstarscatalog')

# Defining of the dataframe
df = pd.DataFrame(columns=['Number', 'Name', 'Identifier', 'Constellation', 'Distance', 'RAJ2000', 'DECJ2000'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    if(columns != []):
        number = columns[0].text.strip()
        name = columns[1].text.strip()
        identifier = columns[2].text.strip()
        constellation = columns[3].text.strip()
        distance = columns[5].text.strip()
        raj2000 = columns[9].text.strip()
        decj2000 = columns[10].text.strip()

        df = df._append({'Number': number, 'Name': name, 'Identifier': identifier, 'Constellation': constellation,
                         'Distance': distance, 'RAJ2000': raj2000, 'DECJ2000': decj2000},
                        ignore_index = True)

#print(df.head())
print(df.info())

df['Distance'].astype('float')

print(df.info())