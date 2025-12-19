import time
import random

print("Welcome to Timed Math Challenge")
operators = ["+","-","*","/"]

Min_operand = int(input("Enter the starting value of Operand: "))
Max_operand = int(input("Enter the Ending value of Operand: "))
Total_problems = int(input("Enter the total Number of Problems:"))

def generate_problem():
    left_operand = random.randint(Min_operand,Max_operand)
    right_operand = random.randint(Min_operand,Max_operand)
    operator = random.choice(operators)
    expr = str(left_operand) + operator + str(right_operand)
    answer = round(eval(expr),2)
    return expr,answer

wrong_answers = 0

input("Press Enter to Continue!")
print("------------------------")

start_time = time.time()

for i in range(Total_problems):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong_answers += 1

end_time = time.time()
actual_time = round(end_time - start_time,2)

print("----------------------------")
print("Nice Job! You have finished in!",actual_time, "secs")
print("Your accuracy:", wrong_answers, "times Answered wrong!")