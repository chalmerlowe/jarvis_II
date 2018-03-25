from dateutil import parser
from datetime import datetime,timedelta

tsset = set()
tslist = []
lastts = ''
maxdelta=0
with open('timestamps.txt') as f:
	tslist = f.read().split('\n')
for ts in tslist:
	if ts!='':
		tsset.add( parser.parse( ts ) )
tslist = sorted( tsset )
for ts in tslist:
	if lastts!='':
		if maxdelta<(ts - lastts).total_seconds():
			maxdelta = (ts - lastts).total_seconds()
	lastts = ts
print('Biggest difference between timestamps is '+str(maxdelta)+' seconds.')
	
	
