
def checkInput(pay):
    try: #check that input can be convert to int type
        ipay=int(pay) 
    except: #if input can not be convert to int type, return error message
        print("Invalid Input!! Please check it")
        exit()
    return ipay #return the input that type of int

def calPayment(pay): #calculate the payment
    refPay = [0, 1200, 4600, 8800, 15000, 30000, 50000] #reference payment
    refRate = [0.06, 0.15, 0.24, 0.35, 0.38, 0.40, 0.42] #reference rate
    tax = 0 #initial tax
    for i in range(6): 
        if (pay > refPay[i] and pay<=refPay[i+1]): #check the range
            tax = pay*refRate[i] #calculate the tax
            #print(tax)
        if (tax!=0) : break
    if (pay>refPay[6]) : tax = pay*refRate[6] #check the exceed ragne
    elif(pay<0) : #check validity
        print("Invalid Input!! Please check it")
        pay = int(input("Pre-tax annual salary : "))
        calPayment(checkInput(pay)) 
    return (pay-tax)

#--------------------------------------main--------------------------

pay = int(input("Pre-tax annual salary : "))
print("After-tax : " + str(calPayment(checkInput(pay))))