import os
import sqlite3

#creates an SQL database and connects to it
conn = sqlite3.connect('test.db')

#creates a table that will hold the text files in the database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )")
    conn.commit()
conn.close()

#gets all the files in the project folder and saves them to a variable. Then, prints the variable containing all the files
fileList = os.listdir(path='C:\\Users\\Owner\\Documents\\Tech Academy Python Projects\\Basic-Python-Projects\\SQL Database Text Files\\')
print(fileList)

#re-opens the connection to the database
conn = sqlite3.connect('test.db')

#if the file in the directory is a .txt file, INSERTs it into the database
with conn:
    cur = conn.cursor()
    for filename in fileList:
        if filename.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_files) VALUES (?)", \
                        (str.split(filename)))
            conn.commit()
            continue
        else:
            continue
conn.close()

#re-opens the connection to the database
conn = sqlite3.connect('test.db')

#displays the contents of the database
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_files FROM tbl_files")
    results = cur.fetchall()
    print(results)
conn.close()


