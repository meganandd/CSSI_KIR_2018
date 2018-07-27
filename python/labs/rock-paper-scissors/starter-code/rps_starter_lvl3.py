#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
tie_count = 0
p_count = 0
c_count = 0

def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    # TODO
    return raw_input("Pick a move: 'r', 'p', or 's'. >>> ")


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    # TODO
    return "rps"[random.randint(0,2)]

def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    # TODO
    if player_move == comp_move:
        return "tie"
    elif (player_move == "r" and comp_move == "s") or \
         (player_move == "s" and comp_move == "p") or \
         (player_move == "p" and comp_move == "r"):
        return "player"
    else:
        return "computer"


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    print ("---SCOREBOARD---")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("Ties: " + str(ties))
    # TODO


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    # TODO
    if short_move == 'r':
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    else:
        return "Scissors"

# Write your code below - make RPS happen using the functions above!

while True:
    play = raw_input("Would you like to play? Type 'y' or 'n'. >>> ")
    if play.lower() == 'y':
        playermove = get_player_move()
        print("Player chose " + get_move_name(playermove) + ".")
        compmove = get_computer_move()
        print("Computer chose " + get_move_name(compmove) + ".")
        winner = determine_winner(playermove, compmove)
        if winner == "player":
            p_count = p_count + 1
        elif winner == "computer":
            c_count = c_count + 1
        else:
            tie_count = tie_count + 1
        print_scoreboard(p_count, c_count, tie_count)
    elif play.lower() == 'n':
        print("Thanks for playing!")
        break
