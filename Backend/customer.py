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
        query = ('select*from customers')
        cursor.execute (query)
        for (SRno,name,address,car,phone_number,age,car_company) in cursor:
            print("----------------------------------------------------------------------")
            print('SRno                              :',SRno)
            print('name                              :',name)
            print('address                           :',address)
            print('car                               :',car)
            print('phone number                      :',phone_number)
            print('age                               :',age)
            print('car company                       :',car_company)
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
        name=input('enter name:')
        address=input('enter address:')
        car=input('enter car:')
        phone_number=input('enter phone number:')
        age=int(input('enter age:'))
        car_company=input('enter car company:')
        sql='insert into customers values(%s,%s,%s,%s,%s,%s,%s)'
        values=(SRno,name,address,car,phone_number,age,car_company)
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
        query='delete from customers where SRno=%s'
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
        query=('select*from customers where SRno=%s')
        rec_srch=(SRno,)
        cursor.execute(query,rec_srch)
        for (SRno,name,address,car,phone_number,age,car_company) in cursor:
            print("----------------------------------------------------------------------")
            print('SRno                              :',SRno)
            print('name                              :',name)
            print('address                           :',address)
            print('car                               :',car)
            print('phone number                      :',phone_number)
            print('age                               :',age)
            print('car company                       :',car_company)
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
        name=input('enter name:')
        address=input('enter address:')
        car=input('enter car:')
        phone_number=input('enter phone number:')
        age=int(input('enter age:'))
        car_company=input('enter car company:')
        query='update customers set SRno=%s,name=%s,address=%s,car=%s,phone_number=%s,age=%s,car_company=%s where SRno=%s'
        data=(SRno1,name,address,car,phone_number,age,car_company,SRno)
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
            print('invalid choice has been entered')
