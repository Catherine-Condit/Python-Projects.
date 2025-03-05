import sqlite3

conn = sqlite3.connect('file_db.db') #connect to SQLite database

cur = conn.cursor() #create cursor object to work with db
cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)") #create table if doesn't already exist

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#filter list to get only files that end with '.txt'
txt_files = [file for file in fileList if file.endswith('.txt')]
#insert each .txt found file name into db
for file in txt_files:
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", (file,))
#commit and save changes to db
conn.commit()

#print to console
print("Qualifying text files:")
for file in txt_files:
    print(file)

#close connection
conn.close()

