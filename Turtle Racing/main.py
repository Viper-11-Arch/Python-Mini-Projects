import turtle
import random
import time

WIDTH = 700
HEIGHT = 600
COLORS = ['red','green','yellow','orange','cyan','blue','brown','pink','purple','black']

def get_number_of_turtles():
    turtles = 0
    while True:
        turtles = input("Enter Number of Turtles: ")
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("Enter an valid Number")
            continue
        if turtles <= 1:
            print("Minimum 2 Turtles are required to Begin the Race")
            continue
        elif turtles > 10:
            print("Exceeds Limit! Maximum of 10 turtles were Allowed")
            continue
        return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = (random.randrange(1,20))
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 10 - 2:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacex = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacex, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title("Turtle Racing")


racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
