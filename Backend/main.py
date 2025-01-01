import bmw
import customers
import employees
import mercedes
import os
A='''select which table to access
1)bmw
2)customers
3)emloyees
4)mercedes
5)exit the program'''

while True:
    print(A)
    B=int(input('enter serial number of tha table to be accessed'))
    if B==1:
        bmw.menubook()
    elif B==2:
        customers.menubook()
    elif B==3:
        employees.menubook()
    elif B==4:
        mercedes.menubook()
    elif B==5:
        os._exit(0)
