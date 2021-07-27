#-*- encoding: utf-8 -*-
def checkScore(score):
    try: #check that input can be convert to int type
        iscore=int(score) 
    except: #if input can not be convert to int type, return error message
        print("Invalid Input!! Please check it")
        exit()
    return iscore #return the input that type of int

def checkName(name):
    try: #check that input can be convert to string type
        sname=str(name) 
    except: #if input can not be convert to string type, return error message
        print("Invalid Input!! Please check it")
        exit()
    return sname #return the input that type of int

def getGrade(score,name): #calculate the grade
    refScore = [0, 60, 65, 70, 75, 80, 85, 90, 95, 100] #reference score
    refGrade = ["F","D","D+","C","C+","B","B+","A","A+"] #reference grade
    grade = "Z"
    
    for i in range(9): 
        if (score >=refScore[i] and score<refScore[i+1]): #check the range
            grade = refGrade[i] #Get a grade
        if (grade!="Z") : break
    
    if (score==refScore[9]) : grade = refGrade[8] #check the exceed ragne
    elif(score<0 or score>refScore[9]) : #check validity
        print("Invalid Score!! Please check it")
        score = int(input("Enter the score(0~100) : "))
        name, score, grade = getGrade(checkScore(score),checkName(name)) 
        
    return name, score, grade
    

#--------------------------------------main----------------------------------

score = input("Enter the score(0~100) : ")
name = input("Enter the name : ")
score, name, grade = getGrade(checkScore(score),checkName(name)) 

print("Name : ",name)
print("Score : ",str(score))
print("Grade : ",grade)
