#Rock, Paper, Scissors Game
#define the rock paper scissors function
def rps(uc):
#import the random module to allow us to play against the computer
    import random
#define the list of options for the computer to pick from
    mylist = ["rock", "paper", "scissors"]
#use the random fuction to pick a random option from the list
    cc = random.choice(mylist)
#if the computer choice equals the users choice, return the string "Draw!"
    if cc == uc:
        return 'Draw!'
#using elif statements to compare the different scenarios, using .upper() to prevent case sensitivity giving an incorrect comparison
    elif cc == 'rock' and uc == 'paper':
        return f'Computer chose: {cc.upper()}, you WON!'
    elif cc == 'paper' and uc == 'scissors':
        return f'Computer chose: {cc.upper()}, you WON!'
    elif cc == 'scissors' and uc == 'rock':
        return f'Computer chose: {cc.upper()}, you WON!'
    else:
        return f'Computer chose: {cc.upper()}, you LOST!'

#Display a welcome/intro message to the user
print("Welcome to Rock, Paper, Scissors!")
#Define a variable which will prompt the user whether they are ready, and compare it to y, if it is not y, the continue will iterate the loop again
ready = False
while ready == False:
    rdy = input("Are you ready to start? (Y/N): ")
    if rdy.lower() == 'y':
        ready = True
    else:
        continue
#Define a loop variable to keep the game going until the player does not want to continue playing
playagain = True
#loop until playagain becomes false
while playagain:
#ask the user for their choice
    userchoice = input("Enter your pick (Rock, Paper, or Scissors): ")
#lower case their input to prevent case sensitivity logic failure
    userchoiceu = userchoice.lower()
    choice = ["rock", "paper", "scissors"]
#check if their input is valid
    if userchoiceu in choice:
#call the rps function to compare this input with the computers input and display the output from the function
        print(rps(userchoiceu))
#ask the user if they want to play again
        pa = input("Would you like to play again? (Y/N): ")
#if the user does not want to play again, break the loop and display game closed
        if pa.lower() == 'n':
            playagain = False
            print('Game Closed!')
#if the user enters anything else, continue playing and iterate through the loop again
        else:
            playagain = True
#catch if the users input is not rock, paper, or scissors
    else:
        print("Invalid Entry Format, Try Again!")


