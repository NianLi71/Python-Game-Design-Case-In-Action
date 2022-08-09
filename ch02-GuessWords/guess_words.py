from ast import While
from cmath import pi
import random

words = ['hello', 'world', 'today', 'tomorrow']

print('Game start!')

while(True):
    pick_a_word = random.choice(words)
    shuffled_word = ''.join(random.sample(pick_a_word, len(pick_a_word)))
    print(f"Here is the word in shuffled order: {shuffled_word}")

    while(True):
        print("What's your guess?")
        you_guess = input()

        if you_guess == pick_a_word:
            print("Wow, you get it!")
            break
        else:
            print("Wrong, please try again!")

    print("Do you want to play a another round?")
    play_again = input()
    if play_again != 'y' and play_again != 'Y':
        break

print("See you next time!")