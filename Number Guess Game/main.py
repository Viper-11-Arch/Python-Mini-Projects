import random
print("Welcome to Number Guessing Game!")

chance_limit = 5

left_limit = int(input("Enter the Left Limit: "))
right_limit = int(input("Enter the Right Limit: "))


random_number = random.randint(left_limit, right_limit)

while chance_limit > 0:
    num = int(input("Enter a Number: "))
    if num == random_number:
        print("🎉Your guess is correct!")
        break
    elif num < random_number:
        print("Your guess is lower! Try Higher📈")
    else:
        print("Your guess is higher! Try Lower📉")
    chance_limit -= 1
    print(f"Chances left: {chance_limit}")

if chance_limit == 0:
    print(f"😓You're out of chances! The Number was {random_number}")
    quit()




