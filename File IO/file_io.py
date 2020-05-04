import os

#displays the current directory where this .py file i
print(os.getcwd())

#opens the text file named "test.txt" in read mode, displays it's contents, then closes the file
def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

#opens the text file named "test.txt" in append mode, and adds text to it, then closes it
def writeData():
    data = '\nHello World!'
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()
