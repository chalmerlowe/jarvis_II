import os

def txtfilter():
    files = []
    for file in os.listdir():
        if 'txt' in file:
            files.append(file)
    return files

txt_files = txtfilter()
print(txt_files)