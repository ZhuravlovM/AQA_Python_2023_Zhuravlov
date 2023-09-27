import psycopg2


connection = psycopg2.connect(user='postgres',
                              password='1',
                              host='localhost',
                              port='5432',
                              database='postgres')

cursor = connection.cursor()
cursor.execute('CREATE TABLE tablewithusers (id varchar(8) primary key, name varchar(25), last_name varchar(25), email varchar(25), age int);')
cursor.execute("INSERT INTO tablewithusers (id, name, last_name, email, age) VALUES "
               "('AAAA', 'ordinary_name', 'ordinary_lastname', 'email@email.com', 30), "
               "('BBBB', 'ordinary_name', 'ordinary_lastname', 'email@email.com', 30);")
cursor.execute('SELECT * FROM tablewithusers;')
connection.commit()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()
