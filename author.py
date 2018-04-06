import sqlite3
import json

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS course;

CREATE TABLE user (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT
);

CREATE TABLE course (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT
);

CREATE TABLE member (
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id,course_id)
);
''')

fname = input("enter filename")
if len(fname) < 1 : fname = "roster_data.json"

fh_str = open(fname).read()
json_data = json.loads(fh_str)

for entry in json_data :
    name = entry[0]
    titl = entry[1]
    role = entry[2]

    cur.execute("INSERT OR IGNORE INTO user (name) VALUES (?)",(name,))
    cur.execute("SELECT id FROM user WHERE name = ?",(name,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO course (title) VALUES (?)",(titl,))
    cur.execute("SELECT id FROM course WHERE title = ?",(titl,))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO member (user_id,course_id,role) VALUES (?,?,?)",(user_id,course_id,role))

    conn.commit()

sqlstr = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X'''

for entry in cur.execute(sqlstr) :
    print(entry[0])
