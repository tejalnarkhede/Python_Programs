import cx_Oracle

con = cx_Oracle.connect('system/1234@localhost:1521/xe')
print(con.version)

cursor = con.cursor()
   
   #Creating a table
cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
print("Table Created")
   

