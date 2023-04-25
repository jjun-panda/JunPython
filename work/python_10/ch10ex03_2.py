import sqlite3

conn = sqlite3.connect('test0420.db')

sql = '''
insert into saram(id, name, age) values ("Kim", "Coding", 28);
'''

c = conn.cursor()
c.execute(sql)

c.close()

conn.commit()
conn.close()