from datetime import datetime
from dateutil.relativedelta import relativedelta

birth = input("When is your birthday? (ex) 2021-07-19) \n")
birth = datetime.strptime(birth, "%Y-%m-%d") #convert to date type(?) from string
today = datetime.now() #Get a date of today automatically

 #Vaildity check
if birth > today: 
    print("Invaild date! Please check the birthday.")
    exit()

#initialization
age_month = 0
age_day = 0

if birth.day <= today.day:
    age_day = today.day - birth.day
else:
    age_day = (today.replace(day=1) - relativedelta(days=1)).day + today.day - birth.day
    today -=relativedelta(months=1)

if birth.month <= today.month:
    age_month = today.month - birth.month
    age_year = today.year - birth.year  
else:
    age_month = 12 + today.month - birth.month
    age_year = today.year - birth.year -1

print(str(age_year)+" years, "+str(age_month)+" months, "+str(age_day)+" days")
print("Your age is " + str(age_year))