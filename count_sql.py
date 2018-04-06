import sqlite3
conn = sqlite3.connect(emaildb.sqlite)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS counts")

cur.execute("CREATE TABLE counts (email TEXT, count INTEGER)")

fname = input("mbox.txt")
fh = open(fname)

for line in fh :
    line = line.strip()
    word = line.split()
    if word[0] is "From:" :
        email = word[1]
        cur.execute("SELECT count FROM counts WHERE email = ?",(email,))
        row = cur.fetchone()
        if row is None :
            cur.execute("INSERT INTO counts (email,count) VALUES (?,1)",(email,))
        else :
            cur.execute("UPDATE counts SET count = count +1 where email = ?",(email,))
    else :
        continue
    conn.commit()

sqlstr = "SELECT * FROM counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr) :
    print(row[0],row[1])
