import psycopg2

connection = psycopg2.connect('dbname=learningsql', user="postgres", password="lkja7890")

# Open a cursor to perform database operations
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE table1(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    );
'''
)


cursor.execute('INSERT INTO table1 (id, completed) VALUES (1, true);')

# commit, so it does the executions on the db and persists in the db
connection.commit()

connection.close()
cursor.close()