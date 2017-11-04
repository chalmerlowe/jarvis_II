import os

files_for_deletion = ['numbers.txt', 'output.txt', 'results.txt', 'buffer.txt']

for file in files_for_deletion:
    try:
        os.remove(file)
        print('Removed: {}'.format(file))
    
    except:
        print('The file: {} could not be found'.format(file))
