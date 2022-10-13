"""
Monty Hall Problem:

    As a personal project, I have decided to model the Monty Hall Problem. As
    I understand the mathematics behind the problem, as there are multiple
    approaches to understand the monty hall problem, using a simplistic
    approach with the total law of probability (which is useful when it comes
    to explaining the solution to a non professional),or using a bayesian
    approach which is more sophisticated and rather formal way of proving.

    I have done this to prove to myself analytically that the math is correct.
    This has been an interesting problem that I found enjoyable to transcribe
    into coding.

    It has to however be considered that the simulation uses pseudo random
    generation which could possibly introduce biases.

    Set up of the game:
        1. Three doors are created and shuffled
        2. A bot chooses a door
        3. A random door that isn't the winning door or the door currently
        picked by the bot is opened and revealed to be a losing door
        4. The bot has an option of switching the door or not which is decided
        via a pseudo-random generator

    Improvements:
        - Diminishing the bias as much as possible
        - Extending the problem where the door revealed can be a winning door
          too
        - General extensions that can be thought of further
        - Possible error calculation

@author: Qi Nohr Chen 26/07/2022
"""

import random
import numpy.random as rnd

TRIALS = 50000 #Trials or games run by the bot

def create_win_prize():
    """
    The function sets up the game. It creates three doors and shuffles them
    using pseudo-random-generation.

    Args:
        none
    Returns:
        shuffled_doors : list

    """

    shuffled_doors = ["W", "L", "L"] #Initial game
    random.shuffle(shuffled_doors)
    return shuffled_doors

def bot_random_choice():
    """
    Using pseudo random number genetors, let the bot choose a door

    Args:
        none

    Returns:
        choice: integer

    """
    choice = rnd.randint(0, 3, 1)
    return choice

def door_removed(doors, bot_choice):
    """
    The function removes one of the doors that isn't a winning door or a door
    that the bot has picked. It has to be a losing door

    Args:
        doors : list
        bot_choice : integers

    Returns:
    door_array : list


    """
    door_array = doors
    for iteration, _ in enumerate(door_array):
        if door_array[iteration] == "L" and iteration != bot_choice:
            door_array[iteration] = "OPENED"
        elif door_array[iteration] == "W" and iteration == bot_choice:
            for num, _ in enumerate(door_array):
                if door_array[num] == "L":
                    door_array[num] = "OPENED"
                    break
        else:
            pass
    return door_array

def door_switch(opened_door, bot_unswitched_choice):
    """

    The function randomly chooses whether the bot wants to switch their choice
    of door.

    Args:
        opened_door : list
        bot_unswitched_choice : integer

    Returns:
        choice : integer

    """

    choice = bot_unswitched_choice
    switch = rnd.randint(0, 2, 1)

    if switch == 1:
        for door, _ in enumerate(opened_door):
            if opened_door[door] != "OPENED" and choice != door:
                choice = door
            else:
                pass
    else:
        pass

    return choice

def win_by_switch(final_doors, new_choice, old_choice):
    """

    Function calculates the type of win, whether it is a win by switch or by
    staying on the same door.

    Args:
        final_doors : list
        new_choice : integer
        old_choice : integer

    Returns:
        statement : boolean

    """

    for door, _ in enumerate(final_doors):
        if final_doors[door] == "W" and new_choice == door and new_choice != old_choice:
            statement = True
        elif final_doors[door] == "W" and new_choice == door and new_choice == old_choice:
            statement = False
        elif final_doors[door] == "W" and new_choice != door and new_choice == old_choice:
            statement = False
        else:
            statement = True
        return statement

def _main_():

    """
    Main function
    """

    game_won_by_switch = 0
    game_won_by_stay = 0

    for _ in range(TRIALS):
        starting_doors = create_win_prize()
        the_bot_choice = bot_random_choice()
        new_doors = door_removed(starting_doors, the_bot_choice)
        the_bot_choice_new = door_switch(new_doors, the_bot_choice)
        boolean = win_by_switch(new_doors, the_bot_choice_new, the_bot_choice)
        if boolean is True:
            game_won_by_switch = game_won_by_switch + 1
        elif boolean is False:
            game_won_by_stay = game_won_by_stay + 1
    print("You have won ", game_won_by_switch, " games by switching")
    print("You have won ", game_won_by_stay, " games by staying")
    print("probability of win by switching: ", game_won_by_switch/TRIALS)
    print("pribability of win by staying: ", game_won_by_stay/TRIALS)

_main_() #running main function in a single line
    