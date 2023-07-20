import pandas as pd 

tables = pd.read_html('https://es.wikipedia.org/wiki/Python')

len(tables)
tables[4]