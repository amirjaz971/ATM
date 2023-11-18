import random


print("welcome to amirjaz ATM")

account={"name":"","password":"","balance":0}
balance=0
while True:
    print("choose the command below")
    print("1.create account")
    print("2.enter account")
    print("3.exit")
    choose=input("enter the number of the command above here: ")

    if choose=="1":
        print("please enter  user_name and password to create account")
        user_name=input("user_name: ")
        password=input("password: ")
        if len(password)<5:
            print("your password must be at least five characters!")
        else:
            print("your account has been created")
            continue
    elif choose=="2":
        try:
         name=input("user_name: ")
         Pass=input("password: ")
        
         if name==user_name and Pass==password:
            while True:

             print("welcome " +user_name)
             print("what is your task")
             print("1.balance")
             print("2.deposit")
             print("3.withdraw")
             print("4.back")
             print("5.pay bills")
             choose2=input("enter number of the task here: ")
             if choose2=="1":
               print("your balance is: "+str(balance)) 
                
             elif choose2=="2":
                deposit=int(input("enter the amount of the money that you want to deposit into your account: "))
                if deposit>0:
                   
                   balance+=deposit
                else:
                   print("the amount of the deposit is undefined!")
                   continue

             elif choose2=="3":
                withdraw=int(input("enter the amount of the money that you want to withdraw from your account: "))
                if withdraw<=balance and withdraw>0 and balance>=0:
                   
                   
                   balance-=withdraw
                else:
                   print("the amount of the withdraw is more than your balance")
                   continue


             elif choose2=="4":
                break
             elif choose2=="5":
                bills=random.randint(100,1000)
                print("your bills cost: "+str(bills))
                print("do you want to pay your bills?")
                answer=input("YES/NO: ")
                if answer.lower()=="yes":
                   if balance>=bills:
                      balance-=bills
                      bills-=bills
                      
                      print("your bills have been paid")
                      print(f"your bills are {bills}")
                   else:
                      print("you don't have enough money to pay your bills!")  


                elif answer.lower()=="no":
                   continue
                else:
                   print("wrong answer")



 



             else:
                print("wrong number")
                continue



         else:
             print("wrong user_name or password!")
             continue
   

        except NameError:
            print("you must have an account first")
            continue
         
    








    elif choose=="3":
        print("have a nice day")
        break
    else:
        print("wrong number!")
        continue




