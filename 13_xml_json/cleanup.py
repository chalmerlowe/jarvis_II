import os

files_for_deletion = ['misc.json', 'misc_neat.json', 'prices.json',
                      'x_stocks.json', 'output.xml']

for file in files_for_deletion:
    try:
        os.remove(file)
        print('Removed: {}'.format(file))
    
    except:
        print('The file: {} could not be found'.format(file))
