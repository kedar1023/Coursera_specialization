
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute(''' CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
''')

list1=['INSERT INTO Ages (name, age) VALUES ("Yassin", 24)',
'INSERT INTO Ages (name, age) VALUES ("Abraham", 25)',
'INSERT INTO Ages (name, age) VALUES ("Kassia", 18)',
'INSERT INTO Ages (name, age) VALUES ("Kori", 13)']

for i in list1:
    cur.execute(i)
    
# # https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

for row in cur.execute(sqlstr):
     print(str(row[0]))

# cur.close()