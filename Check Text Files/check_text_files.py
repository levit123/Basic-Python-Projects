#searches the current director and displays all files that end with the ".txt" extension

import os

#sets the path(s) to search through to the following directory (which is the directory where this project is stored)
fName = os.listdir(path='C:\\Users\\Owner\\Documents\\Tech Academy Python Projects\\Basic-Python-Projects\\Check Text Files\\')
fPath = 'C:\\Users\\Owner\\Documents\\Tech Academy Python Projects\\Basic-Python-Projects\\Check Text Files\\'

paths = os.path.join(fPath, fName[5])

#searches through the directory and checks each file in the directory. If the file has the ".txt" extension, displays the name of the text file
for filename in os.listdir(path='C:\\Users\\Owner\\Documents\\Tech Academy Python Projects\\Basic-Python-Projects\\Check Text Files\\'):
    if filename.endswith('.txt'):
        print(filename)
        print(os.path.getmtime('C:\\Users\\Owner\\Documents\\Tech Academy Python Projects\\Basic-Python-Projects\\Check Text Files\\'))
        continue
    else:
        continue
