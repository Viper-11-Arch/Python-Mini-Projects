import random
print("Welcome To Rock Paper Scissors! Have Fun😍")
options = ["rock","paper","scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print("Computer_plays: ",computer_input)

    if user_input == "rock" and computer_input == "scissors":
        print("You Won")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You Won")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You Won")
        user_wins += 1
    elif computer_input == user_input:
        print("Draw")
    else:
        print("You Lost")
        computer_wins +=  1

print("Total Wins: ",user_wins)
print("Total Computer Wins: ", computer_wins)
print("GoodBye! Have a Nice Day🤍")









