import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import (connection)
import os
import platform

def clrscreen():
    if platform.system()=="Windows":
        print(os.system('cls'))

def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root',passwd='Pranshu',host='localhost',database='automobile_management')
        cursor = cnx.cursor()
        query = ('select*from mercedes')
        cursor.execute (query)
        for (SRno,model,body_type,fuel_type,Class,price,output,acceleration,top_speed) in cursor:
            print("----------------------------------------------------------------------")
            print('SRno                              :',SRno)
            print('model                             :',model)
            print('body type                         :',body_type)
            print('fuel type                         :',fuel_type)
            print('class                             :',Class)
            print('price                             :',price)
            print('output                            :',output)
            print('acceleration                      :',acceleration)
            print('top speed                         :',top_speed)
            print("----------------------------------------------------------------------")
        cursor.close()
        cnx.close()
        print("completed !!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
        cnx.close()
def insertdata():
    try:
        cnx = connection.MySQLConnection(user='root',passwd='Pranshu',host='localhost',database='automobile_management')
        cursor=cnx.cursor()
        SRno=int(input('enter serial number:'))
        model=input('enter model:')
        body_type=input('enter body type:')
        fuel_type=input('enter fuel type:')
        Class=input('enter class of vehicle')
        price=int(input('enter price:'))
        output=input('enter horsepower output:')
        acceleration=float(input('enter acceleration:'))
        top_speed=int(input('enter top speed:'))
        sql='insert into mercedes values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(SRno,model,body_type,fuel_type,Class,price,output,acceleration,top_speed)
        cursor.execute(sql,values)
        cursor.execute('commit')
        cnx.commit()
        cursor.close()
        cnx.close()
        print('data saved successfully')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
        cnx.close()
def deletedata():
     try:
        cnx = connection.MySQLConnection(user='root',passwd='Pranshu',host='localhost',database='automobile_management')
        cursor=cnx.cursor()
        SRno=int(input('enter serial number of the vehicle to be deleted'))
        query='delete from mercedes where SRno=%s'
        del_rec=(SRno,)
        cursor.execute(query,del_rec)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,'record(s) deleted successfully')
     except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
             print('something is wrong with your username or password')
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
             print('database does not exist')
         else:
             print(err)
         cnx.close()
    
    
   
def search():
    try:
        cnx = connection.MySQLConnection(user='root',passwd='Pranshu',host='localhost',database='automobile_management')
        cursor=cnx.cursor()
        SRno=int(input('enter serial number'))
        query=('select*from mercedes where SRno=%s')
        rec_srch=(SRno,)
        cursor.execute(query,rec_srch)
        for (SRno,model,body_type,fuel_type,Class,price,output,acceleration,top_speed) in cursor:
            print("----------------------------------------------------------------------")
            print('SRno                              :',SRno)
            print('model                             :',model)
            print('body type                         :',body_type)
            print('fuel type                         :',fuel_type)
            print('class                             :',Class)
            print('price                             :',price)
            print('output                            :',output)
            print('acceleration                      :',acceleration)
            print('top speed                         :',top_speed)
            print("----------------------------------------------------------------------")
        clrscreen()
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
        cnx.close()
    
            
            
    
def update():
    try:
        cnx = connection.MySQLConnection(user='root',passwd='Pranshu',host='localhost',database='automobile_management')
        cursor=cnx.cursor()
        SRno=int(input('enter serial number of record to be edited:'))
        SRno1=int(input('enter serial number:'))
        model=input('enter model:')
        body_type=input('enter body type:')
        fuel_type=input('enter fuel type:')
        Class=input('enter class of vehicle')
        price=int(input('enter price:'))
        output=input('enter horsepower output:')
        acceleration=float(input('enter acceleration:'))
        top_speed=int(input('enter top speed:'))
        query='update mercedes set SRno=%s,model=%s,body_type=%s,fuel_type=%s,class=%s,price=%s,output=%s,acceleration=%s,top_speed=%s where SRno=%s'
        data=(SRno1,model,body_type,fuel_type,Class,price,output,acceleration,top_speed,SRno)
        cursor.execute(query,data)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount,'record(s) updated successfully')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('database does not exist')
        else:
            print(err)
            cnx.close()
def menubook():
    while True:
        clrscreen()
        print('\t\t automobile management system ')
        print('=================================================')
        print('1. Add record')
        print('2. Display all records')
        print('3. Search record')
        print('4. Delete record')
        print('5. Update record')
        print('6.Exit')
        print('=================================================')
        choice=int(input('enter choice:'))
        if choice==1:
            insertdata()
        elif choice==2:
            display()
        elif choice==3:
            search()
        elif choice==4:
            deletedata()
        elif choice==5:
            update()
        elif choice==6:
            break
        else:
            print('invalid choice has been enetered')
