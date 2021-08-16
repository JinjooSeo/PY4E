import random

gameNumber = 31 #define the game number

def doGameBR():
    ref = [i+1 for i in range(gameNumber)] #reference list
    number = 0 #init for game flag
    print(f"Baskin Robbins {gameNumber}!\nInsert the numbers")
    
    while True : 
        human = input("My turn : ")
        human = list(map(int, human.split())) #list of human's input as type of int
        if checkInput(human,number) == False : #check the validity for input
            continue
        number = human[-1] #get a game flag
        if number < ref[-1] : 
            del ref[:len(human)] #reduce the reference list
        print(f"------------ Current number : {number} ------------")
        
        if number>=ref[-1] : #loose flag
            print("\nYou loose!")
            break
         
        len_computer = random.randint(1,3) 
        if ref[0] == gameNumber : #win case
            print(f"Computer : {ref[0]}")
            print("\nYou win!") #win flag
            break
        elif len(ref) <= 4 : #forcee loose case
            for i in range(len(ref)-1) :
                print(f"Computer : {ref[i]}")
            del ref[:len(ref)-1] #reduce the reference list
            number = ref[0]-1 #get a game flag
        elif len_computer < len(ref) and ref[-1] == gameNumber : #nomal process
            for i in range(len_computer) :
                print(f"Computer : {ref[i]}")
            del ref[:len_computer] #reduce the reference list
            number = ref[0]-1 #get a game flag
        print(f"------------ Current number : {number} ------------")
        
        #print(ref)
    
def checkInput(my, number) :
    if int(my[0]) != number + 1 or len(my) > 3 :
        print("Please check your input is correct or not")
        return False
    if len(my) == 2 and (int(my[1]) - int(my[0]) != 1) :
        print("Please enter the consecutive numbers")
        return False
    if len(my) == 3 and (int(my[2]) - int(my[1]) != 1 or int(my[1]) - int(my[0]) != 1) :
        print("Please enter the consecutive numbers")
        return False
    return True

doGameBR()