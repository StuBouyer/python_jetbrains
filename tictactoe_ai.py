#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:50:29 2020

@author: stu
"""

# all possible winning combinations
winner_position = [[(3, 1), (3, 2), (3, 3)], [(2, 1), (2, 2), (2, 3)], 
                    [(1, 1), (1, 2), (1, 3)], [(3, 1), (2, 1), (1, 1)], 
                    [(3, 2), (2, 2), (1, 2)], [(3, 3), (2,3), (1,3)], 
                    [(3,1) ,(2, 2), (1, 3)], [(3, 3), (2, 2), (1, 1)]]
# Stores the positions occupied by X and O
player_pos = {'X':[], 'O':[]}

    
def load_players(field):
    i = 0 
    for row in range(3, 0, -1):
        for col in range(1, 4):
            if field[i] != " ":
                player_pos[field[i]].append((col,row))
            i += 1

def print_field():
    print("---------")
    for row in range(3, 0, -1):
        print("| ", end="")
        for col in range(1, 4):
            if (col, row) in player_pos['X']:
                print("X ", end="")
            elif (col, row) in player_pos['O']:
                print("O ", end="")
            else:
                print("  ", end="")
        print("|")
    print("---------")

def check_winner(player):
    for test in winner_position:
        if all(pos in player_pos[player] for pos in test):
            return True
    return False

def check_draw():
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False   

def valid_move():
    in_str = input("Enter the coordinates: ").split()
    try:
        move = (int(in_str[0]), int(in_str[1]))
    except ValueError:
        print("You should enter numbers!")
        move = valid_move()
    if move in player_pos['O'] or move in player_pos['X']:
        print("This cell is occupied! Choose another one!")
        move = valid_move()
    elif move[0] > 3 or move[1] > 3:
        print("Coordinates should be from 1 to 3!")
        move = valid_move()
        
    return move 

if __name__ == '__main__':
    field = input("Enter cells: ").replace("_"," ")
    load_players(field)
    print_field()

    if len(player_pos['X']) == len(player_pos['O']):
        curr_player = "X"
    else:
        curr_player = "O"

    move = valid_move()
    player_pos[curr_player].append((int(move[0]),int(move[1])))  
    print_field()

    if check_winner(curr_player):
        print(f"{curr_player} wins")
    elif check_draw():
        print("Draw")
    else:
        print("Game not finished")
    