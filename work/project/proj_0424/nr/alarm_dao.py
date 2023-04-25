import sqlite3

db_file = 'alarms.db'

sql_select_all = '''select * from alarms'''

sql_create_table = '''
    create table IF NOT EXISTS alarms(
    no integer primary key,
    hour TEXT,
    minute TEXT,
    ap TEXT
    )
'''

sql_insert = '''
    insert into alarms(hour, minute, ap)
    values(?, ?, ?)
'''

sql_update = '''update alarms set hour=?, minute=?, ap=? where no=?'''

sql_delete = '''delete from alarms where no=?'''

def create_table() :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_create_table)

    c.close()
    conn.close()
    print("sucess!!!!!!!")

def select_all() :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_select_all)

    List = []
    for s in c.fetchall() :
        List.append(s)

    c.close()
    conn.close()

    return List


def insert_data(data_list) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_insert, data_list)
    c.close()

    conn.commit()
    conn.close()

def delete(no) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_delete, (no,))
    c.close()

    conn.commit()
    conn.close()