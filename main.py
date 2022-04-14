# Author: Jayden Lao
# Title: Treasure Hunt Game
# Date: 11/02/2022

import random


def main_loop():

    # get grid setting from user
    grid_length = 0
    grid_width = 0
    dimension = input("Please enter grid size (i.e. 5x6): ")

    # insert assertion for valid grid size input

    build = ""
    for char in dimension:
        if char != "x":
            build += char
        else:
            grid_length = int(build)
            build = ""

    grid_width = int(build)

    # build grid
    grid = []
    for i in range(grid_length):
        grid.append([])
        for j in range(grid_width):
            grid[i].append("X")

    #print_grid(grid)
    random.seed(0)
    # run game
    score = 0
    player_x = grid_width // 2
    player_y = grid_length // 2

    grid[player_y][player_x] = "P"

    alive = True
    while alive:
        (grid, score, player_x, player_y) = phase(grid, score, player_x, player_y)
        grid[player_y][player_x] = "P"
        if (grid, score, player_x, player_y) == (0, 0, 0, 0):
            alive = False




def phase(g, pts, x, y):

    options = ["UP(U)", "DOWN(D)","LEFT(L)", "RIGHT(R)"]
    # player at bottom row
    if y == len(g):
        options[1] = "X"

    # player at top row
    if y == 0:
        options[0] = "X"

    # player at left column
    if x == 0:
        options[2] = "X"

    # player at right column
    if x == len(g[0]):
        options3 = "X"

    prompt = "What would you do?\n"
    for i in range(len(options)):
        prompt += options[i]+"\n"

    print("<< This is the current map >>\n")
    print_grid(g)
    move = input("\n"+prompt+">> ")

    if move == "U":
        y -= 1
    elif move == "D":
        y += 1
    elif move == "L":
        x -= 1
    elif move == "R":
        x += 1

    draw = random.randint(0, 10)
    if draw < 4:
        print("You stepped on a mine! GAME OVER!")
        return 0, 0, 0, 0
    else:
        val = random.randint(0, 10)
        print(f"You found a treasure! You received {val} points!")
        pts += val
        return g, pts, x, y


def print_grid(g):

    for i in range(len(g)):
        build = ""
        for j in range(len(g[i])):
            build += g[i][j]+" "
            if j == len(g[i]) - 1:
                print(build)


main_loop()
