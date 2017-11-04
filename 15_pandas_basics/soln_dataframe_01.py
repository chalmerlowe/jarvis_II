import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('../15/log_file_na.csv', names=['name',
                                                  'email',
                                                  'fm_ip',
                                                  'to_ip',
                                                  'date_time',
                                                  'lat',
                                                  'long',
                                                  'payload_size'])

payloads = df.payload_size

minimum = payloads.min()
maximum = payloads.max()


print('max minus min', payloads.max() - payloads.min())
#print(minimum, maximum, maximum - minimum)
