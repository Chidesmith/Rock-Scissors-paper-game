
#inports randint
from random import seed
from random import randint
seed(6)

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Make a choice for the computer player
computer = randint( 1,3)

# Get a choice from the user
user = (input("\nEnter your choice: \n1 for Rock, \n2 for Sccissors \n3 for Paper: "))

#Validates the user input 
valid = user.isnumeric()
if valid:
  user = int(user)
  if (user != 1) and (user != 2) and (user != 3):
      print("Invalid Input")
      exit
  else:
#Converts user's intiger inputs to approprate strings
    if user == 1:
      user_choice = "Rock"
    elif  user ==2:
      user_choice = "Scissors"
    elif user ==3:
      user_choice = "Paper"
    if computer ==1:
      computer_choice = "Rock"
    elif computer ==2:
      computer_choice = "Scissors"
    elif computer ==3:
      computer_choice = "Paper"

# Compare the user and computer choice and Print the right message, based on the choices
    if computer == user:
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("It's a draw!")
    elif (computer == 1 and user == 2):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Rock smashes Scissors. You lose!")
    elif (computer == 1 and user == 3):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Paper covers Rock. You win!")
    elif (computer == 2 and user == 1):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Rock smashes Scissors. You win!")
    elif (computer == 2 and user == 3):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Scissors cut Paper. You lose!")
    elif (computer == 3 and user == 1):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Paper covers Rock. You lose!")
    elif (computer == 3 and user == 2):
      print("You choosed ",user_choice)
      print("The Computer Choosed ",computer_choice)
      print("Scissors cut Paper. Youexit win!")
else:
  print("Invalid input")
  exit
   