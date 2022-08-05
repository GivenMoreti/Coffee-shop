import psycopg2
connection = psycopg2.connect(user ="postgres",password="given",dbname="coffeedb",host = "127.0.0.1",port="5432")
print("successfully connected")

# this is the second way to connect postgres with backend/disregard it
# import psycopg2
# #establishing the connection
# conn = psycopg2.connect(
#    database="postgres", user='postgres', password='given', host='127.0.0.1', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
# #Executing an MYSQL function using the execute() method
# cursor.execute("select version()")
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)
# #Closing the connection
# conn.close()
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',

# creating a table 'people'
cursor = connection.cursor()
# add new values into the table people
cursor.execute('DROP TABLE IF EXISTS people')
cursor.execute('''
CREATE TABLE people(
   id INTEGER NOT NULL,
   name VARCHAR(20),
   position VARCHAR(20) NOT NULL);
   ''')
cursor.execute('DROP TABLE IF EXISTS coffee')
cursor.execute('''
CREATE TABLE coffee(
   id INTEGER NOT NULL,
   name VARCHAR(20),
   price FLOAT NOT NULL);
   ''')
sql_people = 'INSERT INTO people(id,name,position)VALUES(%(id)s,%(name)s,%(position)s);'


data_people = {
   'id':'34',
   'name':'wix',
   'position':'admin'
}
sql_people = 'INSERT INTO people(id,name,position)VALUES(%(id)s,%(name)s,%(position)s);'

data_people = {
   'id':'36',
   'name':'wiz',
   'position':'clerk'
}
# fetching data from people

cursor.execute('SELECT * FROM people;')
result = cursor.fetchall() #fetchmany(20) or fetchone() 
print(result)


sql_coffee = 'INSERT INTO coffee(id,name,price)VALUES(%(id)s,%(name)s,%(price)s);'
data_coffee = {
   'id':'24',
   'name':'kofiFI',
   'price':'42'
}
sql_coffee = 'INSERT INTO coffee(id,name,price)VALUES(%(id)s,%(name)s,%(price)s);'
data_coffee = {
   'id':'21',
   'name':'kofila',
   'price':'22'
}
cursor.execute('SELECT * FROM people;')
result = cursor.fetchall() #fetchmany(20) or fetchone() 
print(result)

cursor.execute(sql_people,data_people)
cursor.execute(sql_coffee,data_coffee)
connection.commit()
connection.close()
cursor.close()

print('successfully added new values')