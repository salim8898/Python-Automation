import os

for foldername, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is: ' + foldername)
    for subfolder in subfolders:
        print(subfolder)
    for filename in filenames:
        print(filename)
    
