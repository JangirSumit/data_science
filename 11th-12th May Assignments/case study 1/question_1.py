# 1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT.
# The trace of Robot movement is as given following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after directions are steps.
# Write a program to compute the distance current position after sequence of movements.
# Hint: Use math module.

import math

X = 0
Y = 0


def get_coordinates(string):
    global X
    global Y
    if string[0].upper() == "UP":
        Y += int(string[1])
    elif string[0].upper() == "DOWN":
        Y -= int(string[1])
    elif string[0].upper() == "LEFT":
        X -= int(string[1])
    elif string[0].upper() == "RIGHT":
        X += int(string[1])


list_moves = []

print("Enter ROBOT's movement")
while True:
    move = input("[Enter 1 to end]>>> ")
    list_moves.append(move)

    if move == "1":
        for move in list_moves:
            get_coordinates(move.split(" "))

        distance_from_origin = math.sqrt((X**2)+(Y**2))
        print(f"Distance from Origin : {distance_from_origin}")
        print(f"Final position : ({X}, {Y})")
        break
