import psycopg2

connection = psycopg2.connect('dbname=learningsql', user="postgres", password="lkja7890")

# Open a cursor to perform database operations
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
    CREATE TABLE table1(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    );
'''
)


cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);',(3, True))

SQL = 'INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
 'id':2,
    'completed': False
}
cursor.execute(SQL, data)


# commit, so it does the executions on the db and persists in the db
connection.commit()

connection.close()
cursor.close()