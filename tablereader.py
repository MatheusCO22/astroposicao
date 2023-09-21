import pandas as pd
from bs4 import BeautifulSoup

with open('example.html') as file:
    soup = BeautifulSoup(file, 'html.parser')
tables = pd.read_html(str(soup))