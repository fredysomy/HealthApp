import mysql.connector
co=mysql.connector.connect(host="localhost",user="root",password="student")
c=co.cursor()
try:
    c.execute("use wikisavea")
    def add():
        
    add()    
except:
    c.execute("create database wikisavsae")
    c.execute("use wikisavsae")
    def add():
        print("ass")
    add()   


