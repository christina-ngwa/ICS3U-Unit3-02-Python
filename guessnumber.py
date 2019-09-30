#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# this function checks if the user guess the number 5


import constants


def main():
    # this function checks if the user guess the number 5

    # input
    print("Guess what number I'm thinking of! (between 0 & 9)")
    print("")
    guess = int(input("Enter your guess: "))

    # process
    if guess == constants.myanswer:
        # output
        print("")
        print("You are correct!")


if __name__ == "__main__":
    main()
