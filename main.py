import random

exit = False
user_score = 0
computer_score = 0

def print_score():
    print("Your score is: " + str(user_score))
    print("Computers score is: " + str(computer_score))
    print("-----------------------------------------------------")

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Please select rock, paper, or scissors: \n")
    computer_input = random.choice(options)
    if user_input == "exit":
        print("Game Ended")

        exit = True


    if user_input == 'rock':

        if computer_input == 'rock':
            print("You chose rock")
            print("Computer chose rock")
            print("It's a DRAW!")
            print_score()

        elif computer_input == 'paper':
            print("You chose rock")
            print("Computer chose paper")
            print("you LOSE!")
            computer_score+=1
            print_score()

        elif computer_input == 'scissors':
            print("You chose rock")
            print("Computer chose scissors")
            print("you WIN!")
            user_score+=1
            print_score()

    elif user_input == 'paper':

        if computer_input == 'rock':
            print("You chose paper")
            print("Computer chose rock")
            print("You WIN!")
            user_score+=1
            print_score()

        elif computer_input == 'paper':
            print("You chose paper")
            print("Computer chose paper")
            print("It's a DRAW")
            print_score()

        elif computer_input == 'scissors':
            print("You chose paper")
            print("Computer chose scissors")
            print("you LOSE!")
            computer_score+=1
            print_score()

    elif user_input == 'scissors':

        if computer_input == 'rock':
            print("You chose scissors")
            print("Computer chose rock")
            print("you LOSE!")
            computer_score+=1
            print_score()

        elif computer_input == 'paper':
            print("You chose scissors")
            print("Computer chose paper")
            print("you WIN!")
            user_score+=1
            print_score()

        elif computer_input == 'scissors':
            print("You chose scissors")
            print("Computer chose scissors")
            print("It's a DRAW!")
            print_score()

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid Input!")

