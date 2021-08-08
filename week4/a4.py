def check_id(number) :
    if len(number) != 14 or number.find("-") == -1 or number[6:7]!="-": #validity check
        print("Invaild input! Please check it.")
        runProcess()
    
    #Extract values
    year = str(number[:2])
    month = str(number[2:4])
    day = str(number[4:6])
    gender = str(number[7:8])

    #Check validity
    if gender in ["1","3"] :
        s_gender = "Man"
    elif gender in ["2","4"] :
        s_gender = "Woman"
    else :
        print("Invaild input! Please check it.")
        runProcess()
        
    check_year(year,gender) #check year
    return year, month, day, s_gender

def check_year(year,gender) :
    if(int(year) <=21 & int(year) >=0) :
        q = input("Were you born after 2000? Yes(o) No(x) : ")
        if q == "o" : #born in 2000 ~ 2021
            if gender not in ["3","4"] :
                print("Check input!")
                runProcess()
        elif q == "x" : #born in 1900 ~ 1921
            if gender not in ["1","2"] :
                print("Check input!")
                runProcess()
        else :
            print("Check the response! (o or x)")
            check_year(year,gender)

def runProcess() :
    number = input("Enter your resident registration number : ")
    return check_id(number)
    
#---main---
year,month,day,gender = runProcess()
print(f"Bitrh : {year}.{month}.{day} Gender : {gender}")