import pandas as pd

logs = pd.read_csv('log_file_1000.csv',
                   names=['name', 'email', 
                          'fmip', 'toip', 'datetime', 
                          'lat', 'long', 'payload_size'])

matching_ips = logs.fmip == logs.toip
counts = matching_ips.value_counts()
print('Total number of rows with matching To and From ips:', counts[True])

uniq_payloads = len(logs.payload_size.unique())
print('Total number of unique payloads:', uniq_payloads)

hist_fmip = logs.fmip.value_counts()
print('Highest number of From ips:', hist_fmip.max())
print('Lowest number of From ips:', hist_fmip.min())

print('Columns in logs:')
for item in logs.columns:
    print(item)
  
# this syntax achieves the same thing, but with a bit
#     less fuss. The * syntax unpacks the list-like 
#     logs.columns object into separate values.
# print('Columns in logs:', *logs.columns, sep='\n')


