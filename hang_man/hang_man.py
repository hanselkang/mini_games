# Import sources
# words list
# random
# time

import time
import random
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(board[0], board[1], board[2], board[3], board[4])


hang_man_board = ['_ '] * 5

# First display

name = input("Please write down your name: ")
print(f"Hi,{name}. Let's play Hangman game.")

time.sleep(1)
print("Loading...")
print()
time.sleep(0.5)

# Words list

words = ["dream", "right", "fight", "flood", "water", "melon"]

# Load quiz

# Make list random and select a word
random.shuffle(words)
select_word = random.choice(words)

# Answer
# In case import words, remove space in string
word = select_word[0].strip()

# Guess from player
guess_word = ''

# Chances to play

# Play game


turns = 10
chance = 10
while turns > 0:
    print(display_board(hang_man_board))
    print("Chance =", turns)
    print("Hints =", chance)
    guess = input("Guess a character : ")
    print(guess)
    fail = 0  # if there is no match word
    for char in word:
        if char != guess_word:
            print(f"{char} is right. Guess again.")
            fail += 1

        else:  # success
            time.sleep(2)
            print(".")
            print(".")
            print(".")
            time.sleep(0.5)
            print("Congratualtions! you are correct!")
            break

    # Hint
    chances = 10
    if chance >= chances:
        time.sleep(2)
        print(".")
        print(".")
        print(".")
        time.sleep(0.5)
        print('Hint : {}'.format(random.choice(select_word).strip()))
        chances -= 1

    

    if guess not in word:
        turns -= 1
        print("Ooft, wrong guess!")
        print(f"You have {turns} more chances.")

        if turns == 0:
            print()
            print()
            print("You failed. Hangman shutdown.")
