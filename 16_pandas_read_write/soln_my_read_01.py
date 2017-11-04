sign_Dframe = pd.read_csv('log_file_sign.csv', 
                           names=['name', 'email', 'fmip', 'toip',
                                  'datetime', 'lat', 'long', 'payload'],
                           skiprows=range(0, 1001, 2),
                           sep='!',
                           index_col='datetime')
                           
print(sign_Dframe.loc['2016-01-29T22:27:34':'2016-01-28T22:34:28'])                           