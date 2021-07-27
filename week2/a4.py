 #-*- encoding: utf-8 -*-
def checkAge(age):
    try: #check that input can be convert to int type
        iage=int(age)
    except: #if input can not be convert to int type, return error message
        print("Invalid Input!! Please check it")
        exit()
    return iage #return the input that type of int

def checkPayment(payment):
    try: #check that input can be convert to int type
        spayment=str(payment) 
    except: #if input can not be convert to int type, return error message
        print("Invalid Input!! Please check it")
        exit()
    return spayment #return the input that type of int

def getPay(age,payment): #calculate the payment
    refAge = [0, 8, 14, 20, 75] #reference old
    refCard = [0, 450, 720, 1200, 0] #reference pay of card
    refCash = [0, 450, 1000, 1300, 0] #reference pay of cash
    pay = 0
    
    if(age <0) : #check the validity of age
        print("Invalid Age!! Please check it")
        age = input("Enter the age : ")
        age, payment, pay = getPay(checkAge(age),checkPayment(payment)) 

    if(payment == "card") :
        for i in range(4) : 
            if (age >=refAge[i] and age<refAge[i+1]): #check the range
                pay = refCard[i] #pay
    elif(payment == "cash") :
        for i in range(4) : 
            if (age >=refAge[i] and age<refAge[i+1]): #check the range
                pay = refCash[i] #pay
    else :#check the validity of payment
        print("Invalid payment!! Please check it")
        payment = input("Enter the payment (card, cash) : ")
        age, payment, pay = getPay(checkAge(age),checkPayment(payment)) 
      
    return age, payment, pay
    

#--------------------------------------main----------------------------------
age = input("Enter the age : ")
payment = input("Enter the payment (card, cash) : ")
age, payment, pay = getPay(checkAge(age),checkPayment(payment)) 

print("Age : ",str(age))
print("Payment : ",payment)
print("Pay : ",str(pay))
