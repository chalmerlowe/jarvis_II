import os

files = ['first.db',
         'my_first_sql.db',
         'my_second_sql.db',
         'data.db',
         'customers.db',
         'database01.db',
         ]

for file in files:
    try:
        os.remove(file)
        print('REMOVED:', file)
    except FileNotFoundError:
        print('Could not find:', file)
