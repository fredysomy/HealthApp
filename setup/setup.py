#for creating a database and table 

import mysql.connector as msql
import yaml

db = yaml.load(open('../db.yaml'))
user=db['user']
password=db['password']
con=msql.connect(host="localhost",user=user,passwd=password,database="healthapp")

if con.is_connected():
    
    cur=con.cursor()
    cur.execute("create database healthapp")
    cur.execute("use healthapp")
    cur.execute("create table checking (sno int(6) primary key AUTO_INCREMENT,info text(4294967295))")  #Maximum value possible in a text is 4294967295 
    con.commit()
    
else:
    print('connection error')
    
#Dont change the code cauz changing could affect the making of database
#DATABASE SETUP CODE

