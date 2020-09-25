import pandas as pd 
url = 'https://api.statbank.dk/v1/data/FOLK1A/JSONSTAT'
dst = pd.read_json(url)
dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)

print(dst.iloc[:,1])