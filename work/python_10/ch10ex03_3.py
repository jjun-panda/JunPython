import sqlite3

conn = sqlite3.connect('test0420.db')

sql = '''
delete from saram
'''

c = conn.cursor()
c.execute(sql)
c.close()

conn.commit()
conn.close()