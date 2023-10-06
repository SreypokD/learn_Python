import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'python_access'
username = 'postgres'
pwd      = 'pokpokpok'
port_id  = 5432
conn     = None  
cur      = None


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # cursor is an object that allows you to interact with
                         #  a database and perform various operations

    cur.execute('DROP TABLE IF EXISTS emplyees')
    #create table =========================
    create_script = '''  CREATE TABLE IF NOT EXISTS emplyees (  
                            id          int PRIMARY KEY,
                            name        varchar(40) NOT NULL,
                            salary      int)'''
                   #single quotes (''') or triple double quotes (""") are 
                   # not used to create tables directly. Instead, they are
                   #  typically used for multi-line string literals in programming
                   #  languages like Python.

    cur.execute(create_script)
    print('Create table success!')

    # insert table===========================
    insert_script = 'INSERT INTO emplyees (id, name, salary) VALUES(%s ,%s ,%s)'
    # insert_value = (1, 'pokpok' , 350)
    # cur.execute(insert_script, insert_value)
    insert_value = [(1, 'pokpok' , 350) ,(2, 'denden' , 350) , (3, 'davdav' ,350) , (4, 'hakhak' , 350) , (5, 'yoeryoer' , 350) , (6, 'saisai' , 350) , (7, 'naina' , 350)]
    for recode in insert_value:
        cur.execute(insert_script, recode)

    print('Insert value success!')

    # update record =========================
    update_script = 'UPDATE emplyees SET salary = salary + (salary*0.5)'
    cur.execute(update_script)
    print ('update success!')


    # fectall data============================ 
    cur.execute('SELECT * FROM emplyees')
    for record in cur.fetchall():
        print(record['name'] ,record['salary'])

    # delete record ==========================
    # delete_script = 'DELETE FROM emplyees WHERE id = %s'
    # delete_value = input('Enter the ID to delete: ')
    # cur.execute('SELECT id FROM emplyees WHERE id = %s', (delete_value,))
    # if cur.rowcount == 0:
    #     print('No record found with this ID')
    # else:
    #     cur.execute(delete_script, (delete_value,))
    #     print('Deletion successful for ID =', delete_value)


    # commit() method is used to permanently save changes made within a transaction to the database.
    conn.commit()  
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()