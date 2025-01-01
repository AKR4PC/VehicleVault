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
        query = ('select*from employees')
        cursor.execute (query)
        for (empno,name,post,salary,years_of_service,employe_code,sales_in_month,grade) in cursor:
            print("----------------------------------------------------------------------")
            print('empno                             :',empno)
            print('name                              :',name)
            print('post                              :',post)
            print('salary                            :',salary)
            print('years of service                  :',years_of_service)
            print('employee code                     :',employe_code)
            print('sales in month                    :',sales_in_month)
            print('grade                             :',grade)
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
        empno=int(input('enter employee number:'))
        name=input('enter name:')
        post=input('enter post:')
        salary=int(input('enter salary:'))
        years_of_service=int(input('enter years of service:'))
        employee_code=input('enter employee code:')
        sales_in_month=input('enter sales in the current month:')
        grade=input('enter grade:')
        sql='insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(empno,name,post,salary,years_of_service,employee_code,sales_in_month,grade)
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
        empno=int(input('enter employee number'))
        query='delete from employees where empno=%s'
        del_rec=(empno,)
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
        empno=int(input('enter employee number'))
        query=('select*from employees where empno=%s')
        rec_srch=(empno,)
        cursor.execute(query,rec_srch)
        for (empno,name,post,salary,years_of_service,employe_code,sales_in_month,grade) in cursor:
            print("----------------------------------------------------------------------")
            print('empno                             :',empno)
            print('name                              :',name)
            print('post                              :',post)
            print('salary                            :',salary)
            print('years of service                  :',years_of_service)
            print('employee code                     :',employe_code)
            print('sales in month                    :',sales_in_month)
            print('grade                             :',grade)
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
        empno=int(input('enter employee number of record to be edited:'))
        empno1=int(input('enter employee number:'))
        name=input('enter name:')
        post=input('enter post:')
        salary=int(input('enter salary:'))
        years_of_service=int(input('enter years of service:'))
        employee_code=input('enter employee code:')
        sales_in_month=input('enter sales in the current month:')
        grade=input('enter grade:')
        query='update employees set empno=%s,name=%s,post=%s,salary=%s,years_of_service=%s,employe_code=%s,sales_in_month=%s where empno=%s'
        data=(empno1,name,post,salary,years_of_service,employee_code,sales_in_month,empno)
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
