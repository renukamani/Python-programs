import sqlite3
import re
conn = sqlite3.connect("SQL1.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS counts")

cur.execute("CREATE TABLE counts (org TEXT, count INTEGER)")

fname = "mbox.txt"
fh = open(fname)

for line in fh :
    line = line.strip()
    if not line.startswith('From: '): continue
    words = line.split()
    email = words[1]
    piece = email.split("@")
    y = piece[1]
    x = 'SELECT count FROM counts WHERE org = ?'
    cur.execute(x, (y,))
    row = cur.fetchone()
    if row is None :
        cur.execute("INSERT INTO counts (org,count) VALUES (?,1)",(y,))
    else :
        cur.execute("UPDATE counts SET count = count + 1 WHERE org = ?",(y,))
conn.commit()
sqlstr = "SELECT * FROM counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr) :
    print(row[0],row[1])
