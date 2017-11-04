import pandas as pd
from pandas import DataFrame, Series

ldf = pd.read_csv('left_file.csv')
rdf = pd.read_csv('right_file.csv')

namedf = pd.merge(ldf, rdf, on='name', how='inner')
#print(namedf)

namedf['matchip'] = namedf['fmip'] == namedf['toip']

print()
print(namedf.matchip)
