import sqlite3

conn = sqlite3.connect('kedar1023.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
 CREATE TABLE Counts (org TEXT, count INTEGER)''')

dict1={}
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    domain=pieces[1].split('@') #we want the domain names only so spplitting
    print(domain[1])
    email = domain[1]
    #using dict because we wabt to store the key as the domain names
    if email not in dict1:
            count=1
            dict1[email]=count
    else:
        
        dict1[email]=dict1.get(email,0)+1
            

print(dict1)
for k,v in dict1.items():
#     print(k)        
     cur.execute('SELECT count FROM Counts WHERE org = ? ', (k,))
     row = cur.fetchone()
     if row is None:
         cur.execute('''INSERT INTO Counts (org, count)
                 VALUES (?, ?)''', (k,v))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#                     (email,)) 
conn.commit()

# # https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
 
for row in cur.execute(sqlstr):
     print(str(row[0]), row[1])

cur.close()

