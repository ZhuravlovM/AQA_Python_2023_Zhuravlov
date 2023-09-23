import psycopg2


connection = psycopg2.connect(user='***',
                              password='***',
                              host='***',
                              port='***',
                              database='***')

cursor = connection.cursor()
cursor.execute('CREATE TABLE testtable (name varchar(25), age int);')
cursor.execute("INSERT INTO testtable (name, age) VALUES ('ordinary_name', 30), ('unordinary_name', 20);")
cursor.execute('SELECT * FROM testtable;')
connection.commit()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()