import sqlite3

#makes a connection to the database "test.db"
conn = sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    #creates the table "tbl_personS" in the database
    our.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    #INSERTs a person's info into the "tbl_persons" table in the database
    our.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    #INSERTs a person's info into the "tbl_persons" table in the database
    our.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sally', 'May', 'sallymay@gmail.com'))
    #INSERTs a person's info into the "tbl_persons" table in the database
    our.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Kevin', 'Bacon', 'kbacon@rocketmail.com'))
    conn.commit()
conn.close()
    
conn = sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    #runs a SELECT statement to display the entries in the "tbl_persons" table that have the first name "Sarah"
    our.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    #gets all the data in the database and saves it to a variable named "varPerson"
    varPerson = our.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
        print(msg)
        
