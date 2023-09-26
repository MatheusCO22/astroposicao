from bs4 import BeautifulSoup
import requests
import pandas as pd

def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    #return df.applymap(trim_strings)
    return df.map(trim_strings)
    
def get_dataframe():
    with open('./assets/catalog.html') as file:
        soup = BeautifulSoup(file, 'html.parser')

    table = soup.find('table', class_='brightstarscatalog')

    df = pd.DataFrame(columns=['Number', 'Name', 'Identifier', 'Constellation', 'Distance', 'RAJ2000', 'DECJ2000'])

    for row in table.tbody.find_all('tr'):    
        columns = row.find_all('td')
        if(columns != []):
            number = columns[0].text.strip()
            name = columns[1].text.strip()
            identifier = columns[2].text.strip()
            constellation = columns[3].text.strip()
            distance = columns[5].text.strip()
            raj2000 = columns[9].text.strip()
            decj2000 = columns[10].text.strip()

            df = df._append({'Number': number, 'Name': name, 'Identifier': identifier,
                             'Constellation': constellation, 'Distance': distance,
                             'RAJ2000': raj2000, 'DECJ2000': decj2000}, ignore_index = True)

    df = trim_all_columns(df)

    df = df.astype({"Number": int, "Name": str, "Identifier": str, "Constellation": str, "Distance": float,
                    "RAJ2000": str, "DECJ2000": str})
    
    return df