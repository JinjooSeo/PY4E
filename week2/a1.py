import random #import to use random function

def checkInput(human):
    try: #check that input can be convert to int type
        ihuman=int(human) 
    except: #if input can not be convert to int type, convert the input manually.
        if (human == "rock"): ihuman = 0
        elif (human == "scissors"): ihuman = 1
        elif (human == "paper"): ihuman = 2
        else: 
            print("Invalid Input!! Please check it")
            exit()
    return ihuman #return the input that type of int

#play the game
def doGame(human):
    computer = random.randint(0,2)
    if (human>=3): #validity check
        print("Invalid Input!! Please check it (0~2)")
        human = input("Rock Scissors Paper! : ")
        doGame(checkInput(human))
    elif (human==computer): #case : draw
        printStatus(human,computer) #print the status
        print("Draw!")
        endGame() #ask quit or play again
    
    #Calculate the levicivita since the game is based on the permutation
    #Rock(0) -> Scissors(1) -> Papaer(2) -> Rock(0) ->.... 
    levicivita = lambda i,j,k:(i-j)*(j-k)*(k-i)/2 
    other=[0,1,2] #remain component of levicivita calcaulation
    other.remove(int(human))
    other.remove(int(computer))
    levi=levicivita(human,computer,other[0])
    
    if(levi == 1): #case : win
        printStatus(human,computer) #print the status
        print("You Win! Congratutaion :)")
        endGame() #ask quit or play again
    elif(levi == -1): #case : loose
        printStatus(human,computer) #print the status
        print("You Loose :(") 
        endGame() #ask quit or play again

#ask quit or play again
def endGame():
    endgame = int(input("Do you want to play again? (YES->1, No->0) : ")) #Since return value of input function is string, the process of converting to int is needed
    if (endgame == 1):
        human = input("Rock Scissors Paper! : ")
        doGame(checkInput(human))
    elif( endgame == 0): 
        exit()
    else:
        print("Invalid input!! Please check it")
        endGame()

#print the status
def printStatus(human,com):
    a=0 #for Indexing
    for tmpinput in [str(human), str(com)]:
        if (tmpinput == "0"): soutput = "rock"
        elif (tmpinput == "1"): soutput = "scissors"
        else: soutput="paper"
        if (a==0): 
            print(f"You : {soutput}")
            a=a+1 #for indexing
        else: print(f"Computer : {soutput}")


#-----------------------------------main--------------------------------------
print("------------------------ROCK SCISSORS PAPER ------------------------")
print("------Please enter the input as 0(rock), 1(scissors), 2(paper)------")

human = input("Rock Scissors Paper! : ")
doGame(checkInput(human))