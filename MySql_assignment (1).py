## MySql Assignment

## *Question no. 1 :-
## Database is a structured collection of data that is stored in a way that allows for efficient retrieval, and manipulation of data
## SQL database are relational database which eans they use a structured schema to define the tables, coloumns and relationship between data
## NoSQL database use various data models, including documents , keyvalue, column_famiy and graph among others, NoSQl databases are schema-less or schema-flexible.

## *Question no. 2:-
## DDL stands for Data Defination Language,which is a subset of SQL used to define and manage the structure of database objects.DDL statements are for modifying, creating etc
##CREATE : CREATE statement is used to create new database objects, such as tables, indexes etc
## for example

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists file")
mycursor.execute("CREATE TABLE if not exists file.student_table(Studen_name VARCHAR(50),Student_Id VARCHAR(50),ROLL_NO INT,Gender VARCHAR(40));")
mydb.close()

## ALTER statement is used to modify the structure of an existing database object, such as adding, modifying etc.
## for example
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor= mydb.cursor()
mycursor.execute("ALTER TABLE file.student_table ADD COLUMN Student_surname VARCHAR(255);")

## DROP statemnent is used to delete existing database obects, including tables. views etc 
## for example
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  database="mydatabase"
  )
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE file.student_table")  

## TRUNCATE statement is used to clear all the data from a MySql table
# for example:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  database="mydatabase"
  )
mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE file.student_table")

## Question no. 3:
# DML stands for Data Manipulation Language used for managing and manipulating data stored in a relational database management system
# DML is resposible for performing operations as inserting, updating , deleting etc.

#INSERT is used to insert data in the table of database
# for ex
import mysql.connector
mybd = mysql.connector.connect(
    host = "localhost",
    user="abc",
    password="password"
)
print(mybd)
mycursor= mybd.cursor()
mycursor.execute("insert into file.student_table values ('srushti', '01', 10,'female','kalambe')")
mycursor.execute("insert into file.student_table values ('ashu', '02', 12,'male','abc')")
mycursor.execute("insert into file.student_table values ('rahul', '03', 11,'male','thg')")
mycursor.execute("insert into file.student_table values ('riya', '04', 14,'male','yju')")
mybd.commit()
mybd.close()

#UPDATE is used to add new records to a table. you can change the values of one or ore coloumns based on specific coditions
import mysql.connector
mybd = mysql.connector.connect(
    host = "localhost",
    user="abc",
    password="password"
)
print(mybd)
mycursor= mybd.cursor()
mycursor.execute("UPDATE file.student_table SET Student_surname = 'sonawane' WHERE Student_surname ='thg'")
mybd.commit()

## delete is used to delete any inserted data/records from th table
# for ex
import mysql.connector
mybd = mysql.connector.connect(
    host = "localhost",
    user="abc",
    password="password"
)
print(mybd)
mycursor= mybd.cursor() 
mycursor.execute("DELETE FROM file.student_table WHERE Studen_name = 'riya'")
mybd.commit()
print(mycursor.rowcount, 'record(s) deleted')

## Question no. 4:
## DQL stands for Data Query Language. It is used for retrieving and quesying data from relational database management system. 
## SELECT statement is used to retrieve data from oe or more tables in a database. It allows you to specify which columns you want to retrieve
# for ex:
import mysql.connector
mybd = mysql.connector.connect(
    host = "localhost",
    user="abc",
    password="password"
)
print(mybd)
mycursor= mybd.cursor() 
mycursor.execute("SELECT * FROM file.student_table")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

## Question no. 5
## Primary key is a column or a set of columns in a database table that uniquely identifies each record in that table

## Foreign key is a column or a set in one table that is used to establish a link between the data in two tables. It creates a relationship between the tables

## Question no. 6:
#A python code to connect MySql to python:
import mysql.connector # firstly import mysql.connector module
#then create a connection to mysql database by providing the host,username, password
mybd = mysql.connector.connect(
  host = "localhost",
  user = "abc",
  password = "password"
)
#cursor method
# create a cursor object to interact with the database
mycursor = mybd.cursor()
#excute method
mycursor.execute("SELECT * FROM file.student_table")
result = mycursor.fetchall()
for x in result:
  print(x)

## Question no. 7:
# The order of execution in Sql clauses in an sql query
# FROM clause,
# WHERE clause
# HAVING cluase
# SELECT clause
# DISTINCT clause
# ORDER BY clause
# LIMIT/OFFSET  clause
 
