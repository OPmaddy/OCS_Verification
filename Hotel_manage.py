import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


   #Create database

conn=mysql.connector.connect(host='localhost',user='root',password='')
cursor=conn.cursor()
query="create database hotel_management"
cursor.execute(query)
conn.commit()

   #Create user info table

conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
cursor=conn.cursor()
query="create table user_info(userid int(20),username char(60),password int(20),address varchar(10000),mobile_number varchar(10000),ewallet_balance int(255))"
cursor.execute(query)
conn.commit()

   #Create Staff management table

conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
cursor=conn.cursor()
query="create table staff_info(staffid int(100),Name char(100),password int(100),Date_of_birth varchar(100),Working_as char(100),Address varchar(10000),mobile_number varchar(10000),salary int(255))"
cursor.execute(query)
conn.commit()


   #Insert sample data
conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
cursor=conn.cursor()

query="insert into staff_info values(1000,'jagannath',1001,'23/11/01','guard','245-narayan colony vidyadhar nagar','9474744443',15000);"
cursor.execute(query)

query="insert into staff_info values(1001,'shankar',1002,'23/11/01','guard','229-narayan colony vidyadhar nagar','9434959543',15000);"
cursor.execute(query)

query="insert into staff_info values(1002,'gautam',1002,'12/01/01','cook','4/5 dhanshree tower vidyadhar nagar','9435538543',25000);"
cursor.execute(query)

query="insert into staff_info values(1003,'naveen',1004,'12/05/01','cook','241 brahmpuri jagatpura','9435534543',25000);"
cursor.execute(query)

query="insert into staff_info values(1004,'rahul',1005,'12/05/01','room assistant','346 brahmpuri jagatpura','9435534563',10000);"
cursor.execute(query)

query="insert into staff_info values(1005,'ravi',1005,'12/05/01','room assistant','123 brahmpuri jagatpura','9478553463',10000);"
cursor.execute(query)

query="insert into staff_info values(1006,'ram',1007,'12/05/01','room assistant','123 brahmpuri jagatpura','9478553463',10000);"
cursor.execute(query)
conn.commit() 



def user_register():
    
    conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
    cursor=conn.cursor()
    print("Hello New User")
    userid=int(input("create your user id (4 digit id)"))
    username=input("Enter your first name")
    password=int(input("Create a 4 digit pin"))
    address=input("Enter your permanent address")
    mobile_number=int(input("Enter your mobile number"))
    ewallet_balance=0
    query="insert into user_info values({},'{}',{},'{}',{},{})".format(userid,username,password,address,mobile_number,ewallet_balance)
    cursor.execute(query)
    conn.commit()
    
    print("Thank You "+str(username)+" for joining our server ")
    rechoice=input("To register more users press Y ,else press N")
    if(rechoice=='Y'):
        user_register()
    elif(rechoice=='N'):
        return()
    else:
        return()
        
    

def ewallet_recharge(userid):
    
 conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
 cursor=conn.cursor()
 a=int(input("Enter 4 digit mastercode (Only admin can add money)"))
 
 query="select* from user_info where userid={}".format(userid)
 cursor.execute(query)
 conn.commit
 list1=cursor.fetchall()
 k=1234
 if(a==k):
        
     ewallet_balance= list1[0][5]
     deposit=int(input("Enter the amount you want to deposit"))
     query="update user_info set ewallet_balance={}+{} where userid=({})".format(ewallet_balance,deposit,userid)
     cursor.execute(query)
     conn.commit()
     
     print("Your money is successfully deposited")

     
     rechoice=input("To add money again press Y ,else press N")
     if(rechoice=='Y'):
         ewallet_recharge()
     elif(rechoice=='N'):
         return()
     else:
         return()
    
 else:
        
      print("Incorrect password")

      rechoice=input("To add money again press Y ,else press N")
      if(rechoice=='Y'):
        ewallet_recharge()
      elif(rechoice=='N'):
        return()
      else:
        return()

def check():
    
 choice=input("What do you want to check ;for registered mobile no. press M,for address  press A,for ewallet balance press E ")
    
    
 if(choice=='M'):
      print("Your registered mobile number is --> ",list1[0][4])

      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        check()
      elif(rechoice=='N'):
        return()
      else:
        return()

        
 elif(choice=='A'): 
      print("Current Address -->",list1[0][3])

      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        check()
      elif(rechoice=='N'):
        return()
      else:
        return()

 elif(choice=='E'):
      print("Your ewallet balance is -->",list1[0][5])

      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        check()
      elif(rechoice=='N'):
        return()
      else:
        return()
        
 else:
      print("wrong input")

      rechoice=input("To check data press Y ,else press N")
      if(rechoice=='Y'):
        check()
      elif(rechoice=='N'):
        return()
      else:
        return()

def update():

 choice=input("What do you want to update ;for registered mobile no. press M ,for address  press A")

 if(choice=='M'):
         
      x= input("Your mobile number is ")
      query="update user_info set mobile_number='{}' where userid={}".format(x,userid)         
      cursor.execute(query)        
      conn.commit()
         
      print("Data Updated")
         
      rechoice=input("To update more info press Y ,else press N")
      if(rechoice=='Y'):
        update()
      elif(rechoice=='N'):
        return()
      else:
        return()
    
 elif(choice=='A'):
        
      y= input("Your address is ")         
      query="update user_info set address='{}' where userid={}".format(y,userid)         
      cursor.execute(query)         
      conn.commit()
         
      print("Data Updated")

      rechoice=input("To update more info press Y ,else press N")
      if(rechoice=='Y'):
        update()
      elif(rechoice=='N'):
        return()
      else:
        return()

 else:
      print("wrong input")

      rechoice=input("To update info press Y ,else press N")
      if(rechoice=='Y'):
        update()
      elif(rechoice=='N'):
        return()
      else:
        return()

def delete():

    conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
    cursor=conn.cursor()
    userid=int(input("Confirm your 4 digit user id"))
    a=int(input("Confirm your 4 digit pin"))
    query="select* from user_info where userid={}".format(userid)
    cursor.execute(query)
    
    list7=cursor.fetchall()
    
    key=list7[0][2]
    if(a==key):
        
        choice=input("Do you want to delete you account,If yes press Y")        
        if(choice=='Y'):
            
         query="delete from user_info where userid={}".format(userid)
         cursor.execute(query)        
         conn.commit()

         print("All your information has been deleted from the server")
         
        else:
            
         print('Wrong input')

    else:
        
        print("Wrong password")

def emp_resign():

    conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
    cursor=conn.cursor()
    staffid=int(input("Confirm your 4 digit user id"))
    a=int(input("Confirm your 4 digit pin"))
    
    query="select* from staff_info where staffid={}".format(staffid)
    cursor.execute(query)
    list2=cursor.fetchall()
    
    key=list2[0][2]
    
    if(a==key):
        
        choice=input("Do you want to resign,If yes press Y")
        
        if(choice=='Y'):
            
         query="delete from staff_info where staffid={}".format(staffid)
         cursor.execute(query)
         conn.commit()
         print("All your information has been deleted from the server")
         
        else:
            
         print('Wrong input')

    else:
        print("Wrong password")


def staff_check():
    
 choice=input("What do you want to check ;for registered mobile no. press M ,for salary press S,for address  press A")
    
    
 if(choice=='M'):
    
      print("Your registered mobile number is ",list3[0][6])

      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        staff_check()
      elif(rechoice=='N'):
        return()
      else:
        return()
    
 elif(choice=='S'):
        
      print("Your Salary is ",list3[0][7])
        
      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        staff_check()
      elif(rechoice=='N'):
        return()
      else:
        return()
    
 elif(choice=='A'):
         
      print("Current Address -->",list3[0][5])

      rechoice=input("To check more data press Y ,else press N")
      if(rechoice=='Y'):
        staff_check()
      elif(rechoice=='N'):
        return()
      else:
        return()
    
 else:
         
      print("wrong input")

      rechoice=input("To check data press Y ,else press N")
      if(rechoice=='Y'):
        staff_check()
      elif(rechoice=='N'):
        return()
      else:
        return()


def staff_update():
    
 choice=input("What do you want to update ;for registered mobile no. press M ,for address  press A")
      
 if(choice=='M'):
         
       x= input("Your mobile number is ")
       query="update staff_info set mobile_number='{}' where staffid={}".format(x,staffid)
       cursor.execute(query)
       conn.commit()
         
       print("Data Updated")

       rechoice=input("To update more info press Y ,else press N")
       if(rechoice=='Y'):
        staff_update()
       elif(rechoice=='N'):
        return()
       else:
        return()
         
 elif(choice=='A'):
          
       y= input("Your address is ")
       query="update staff_info set address='{}' where staffid={}".format(y,staffid)
       cursor.execute(query)
       conn.commit()
         
       print("Data Updated")

       rechoice=input("To update more info press Y ,else press N")
       if(rechoice=='Y'):
        staff_update()
       elif(rechoice=='N'):
        return()
       else:
        return()

 else:
       print("wrong input")
        
       rechoice=input("To update more info press Y ,else press N")
       if(rechoice=='Y'):
        staff_update()
       elif(rechoice=='N'):
        return()
       else:
        return()

def ewallet_pay():

     conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
     cursor=conn.cursor()
     userid=int(input("Enter your 4 digit user id"))
     a=int(input("Enter your 4 digit pin"))
     query="select* from user_info where userid={}".format(userid)
     cursor.execute(query)
     list1=cursor.fetchall()
     
     key=list1[0][2]
     
     if(a==key):

      ewallet_balance= list1[0][5]
      
      if(ewallet_balance<bill):
          
       print("Insufficient Balance Please recharge ewallet and pay at cash counter rupees "+str(bill))
       
       print("Current Balance-->",ewallet_balance)
       
       ewallet_recharge(userid)

      else:
       query="update user_info set ewallet_balance={}-{} where userid=({})".format(ewallet_balance,bill,userid)
       cursor.execute(query)
       conn.commit()
       print("Your Payment was succesfull ")
      
     else:
      print("Incorrect password")

def feedback():
    
    d={'Name':['Madhav'],'Feedback':['Good']} 
    feedback=pd.DataFrame(d)
    name=input("Please enter your name")
    f=input("Please enter your feedback")
    d1={'Name':[name],'Feedback':[f]}
    feedback1=pd.DataFrame(d1)
    feedback=feedback.append(feedback1)
    
    print(feedback)


    
#MAIN PROGRAM



while(True):
    conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
    cursor=conn.cursor()
    query="select now()"
    cursor.execute(query)
    list9=cursor.fetchall()
    conn.commit()

    a=list9[0][0]

    
    print("         Welcome to Hotel                ")

    print("Date and Time "+str(a)) 
    
    print("To register as new user user press 1")
    
    print("To login as existing user press 2")
    
    print("To login as staff member press 3")
    
    print("To order food press 4")

    choice=int(input("Your choice is "))
    
    if(choice==1):
        user_register()

    elif(choice==2):
     print("       User Login          ")

     conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
     cursor=conn.cursor()
     userid=int(input("Enter your 4 digit user id"))
     
     a=int(input("Enter your 4 digit pin"))
    
     query="select* from user_info where userid={}".format(userid)
     cursor.execute(query)
    
     list1=cursor.fetchall()
     key=list1[0][2]
     if(a==key):
        print("to recharge ewallet type 2")
        
        print("to check details type 3 ")
        
        print("to update details type 4")
        
        print("to give feedback type 5")
        
        print("to delete your account press 6")
        
        choice=int(input("Enter Your choice"))
        if(choice==2):
         ewallet_recharge(userid)   
        elif(choice==3):
         check()
        elif(choice==4):
         update()
        elif(choice==5):
         feedback()
        elif(choice==6):
         delete()
        else:
         print("end")
     
     else:
       print("Incorrect password")

    elif(choice==3):
        print("       Staff Login        ")

        conn=mysql.connector.connect(host='localhost',user='root',password='',db='hotel_management')
        
        cursor=conn.cursor()
        
        staffid=int(input("Enter your 4 digit user id"))
        
        a=int(input("Enter your 4 digit pin"))
    
        query="select* from staff_info where staffid={}".format(staffid)
        cursor.execute(query)
        list3=cursor.fetchall()
        key=list3[0][2]
        if(a==key):
            
          print("to check details type 3 ")
          
          print("to update details type 4")
          
          print("to resign type 5")
          
          choice=int(input("Enter Your choice"))

          if(choice==3):
            staff_check()
          elif(choice==4):
            staff_update()
          elif(choice==5):
            emp_resign()            
          else:
            print("end")

        else:
         print("Incorrect password")

    elif(choice==4):
       menu=pd.read_csv("D:\ip\image\Food.csv")
    
       print(menu)

       f=int(input("Enter the number of items you want to order "))
       k=0
       bill=0
       cal=0
       bill2=pd.DataFrame({'Price':[],'Calorie':[]},index=[])
       while(k!=f):

        q=int(input("Enter itemcode of item number "+str(k+1)+" "))
        i=int(input("Enter the number of plates "))
        name=menu.iloc[q-1,1]
        n=menu.iloc[q-1,2]
        m=menu.iloc[q-1,3]
        cal=(m*i)
        price=(n*i)
        bill2.loc[str(name)]=[price,cal]
        bill=(n*i)+bill
        k=k+1


       print(bill2)
       print("Please pay rupees",bill)
       
       print("To pay through ewallet press 1, to pay as cash press 2")

       choice_=int(input("Enter you choice"))

       if(choice_==1):
          ewallet_pay()
          bill2.plot(kind='pie',y='Calorie',title='Calorie Distribution',legend=False)
          bill2.plot(kind='bar',y='Calorie',title='Calorie Distribution',legend=False)          
          plt.show()

       else:
          print("Please pay at cash counter") 
          bill2.plot(kind='pie',y='Calorie',title='Calorie Distribution',legend=False)
          bill2.plot(kind='bar',y='Calorie',title='Calorie Distribution',legend=False)
          plt.show()
    

          

    else:
         print("end")


    



    


