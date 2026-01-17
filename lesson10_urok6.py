import sqlite3

connection = sqlite3.connect("pet_DB.sl3",5)
cur = connection.cursor()
cur.execute("INSERT INTO info_pet (name,type,age) VALUES ('Gaben','human', '10');")
cur.execute("INSERT INTO info_pet (name,type,age) VALUES ('Grisha','dog', '5');")
cur.execute("INSERT INTO info_pet (name,type,age) VALUES ('Google','cat', '3');")
cur.execute("INSERT INTO info_pet (name,type,age) VALUES ('Door','axolotl', '7');")
connection.commit()
connection.close()