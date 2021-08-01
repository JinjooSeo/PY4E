def checkInput(number) :
    try :
        inumber = int(number)
    except :
        print("Invaild input! Please check it")
    return inumber

def calMult(number) :
    if number > 50 :
        print("Invaild Input! Please checm it (1~50)")
        number = input("Which order do you want to calculate the multiplication table? ")
        calMult(checkInput(number))
    print("Order : "+str(number))
    a = 1 #increase order
    i = 1 #index for odd n
    result = number * 1 #initialization
    while result<=50 : #print the results below the 50
        print(f"{number}X{a}={result}") #print
        a = 2*i + 1 # odd number
        result = number * a
        i=i+1

number = input("Which order do you want to calculate the multiplication table? ")
calMult(checkInput(number))
