"""A template for a python script deliverable for INST326.
Navigator: None
Assignment: Template INST326
Name: Adharsh Maheswaran
Date: 2_10_23
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import os


def determine_winner(p1, p2):
    # insert code and docstrings here

    # Checks the comparison between rock paper and scissors

    if p1 == p2:
        return 'tie'
    elif (p1 == 'r' and p2 == 's') or (p1 == 'p' and p2 == 'r') or (p1 == 's' and p2 == 'p'):
        return 'player1'
    else:
        return 'player2'
    pass


def main(p1_name, p2_name):
    # insert code and docstrings here

    # Enter player input
    p1 = input("Enter player 1's hand shape ('r', 'p', or 's'): ")
    p2 = input("Enter player 2's hand shape ('r', 'p', or 's'): ")

    # Takes in player information and gives output
    outcome = determine_winner(p1, p2)

    # Checks the outcome and print the message
    if outcome == 'player1':
        print(p1_name, "wins!")
    elif outcome == 'player2':
        print(p2_name, "wins!")
    elif outcome == 'tie':
        print("Tie!")
    else:
        print('error')
    pass


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    # For the sake of readability it is important to insert comments all throughout.
    # Complicated operations get a few lines of comments before the operations commence.
    # Non-obvious ones get comments at the end of the line.
    # For example:
    # This function uses the argparse module in order to parse command line arguments.
    parser = argparse.ArgumentParser()  # Create an ArgumentParser object.
    # Then we will add arguments to this parser object.
    # In this case, we have a required positional argument.
    # Followed by an optional keyword argument which contains a default value.
    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
    args = parser.parse_args(args_list)  # We need to parse the list of command line arguments using this object.
    return args


if __name__ == "__main__":
    # If name == main statements are statements that basically ask:
    # Is the current script being run natively or as a module?
    # It the script is being run as a module, the block of code under this will not be executed.
    # If the script is being run natively, the block of code below this will be executed.
    arguments = parse_args(sys.argv[1:])  # Pass in the list of command line arguments to the parse_args function.
# The returned object is an object with those command line arguments as attributes of an object.
# We will pass both of these arguments into the main function.
# Note that you do not need a main function, but you might find it helpfull.
# You do want to make sure to have minimal code under the 'if __name__ == "__main__": ' statement.
main(arguments.p1_name, arguments.p2_name)
