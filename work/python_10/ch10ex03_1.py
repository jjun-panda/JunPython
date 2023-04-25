import sqlite3

conn = sqlite3.connect('test0420.db')

print(conn)
sql = '''create table if not exists saram (
no inreger primary key,
id varchar(20),
name varchar(20),
age integer
)'''

c = conn.cursor()
c.execute(sql)

c.close()
conn.close()