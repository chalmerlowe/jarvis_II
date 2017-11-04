import json

with open('data.json') as inputfile:
    data = json.load(inputfile)
    
if '13.37' in data['NVY']:
    i = data['NVY'].index('13.37')
    print(i, data['NVY'][i])
    
