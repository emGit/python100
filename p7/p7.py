import random

import hangman_art
import hangman_words
from util import macro

def start():
    # p0()
    # p1()
    # p2()
    # p3()
    p4()

def p0():
    macro.moduleStart("1")
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    guess = input("Choose a letter: ").lower()
    for i in chosen_word:
        if i == guess: print("Right")
        else: print("Wrong")

def p1():
    macro.moduleStart("2")
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(f'Pssst, the solution is {chosen_word}.')
    display = []
    word_length = len(chosen_word)
    for _ in range(word_length): display += "_"
    guess = input("Choose a letter: ").lower()
    for i in range(word_length):
        if chosen_word[i] == guess: display[i] = guess
    print(display)

def p2():
    macro.moduleStart("3")
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(f'Pssst, the solution is {chosen_word}.')
    display = []
    word_length = len(chosen_word)
    for _ in range(word_length): display += "_"

    while '_' in display:
        guess = input("Choose a letter: ").lower()
        for i in range(word_length):
            if chosen_word[i] == guess: display[i] = guess
        print(display)
    print("You win!")

def p3():
    macro.moduleStart("4")
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(f'Pssst, the solution is {chosen_word}.')
    display = []
    word_length = len(chosen_word)
    for _ in range(word_length): display += "_"
    lives = 6

    while '_' in display:
        clear()
        guess = input("Choose a letter: ").lower()
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print(hangman_art.stages[lives])
                print(display)
                print("You lose!")
                exit()
        for i in range(word_length):
            if chosen_word[i] == guess: display[i] = guess
        print(hangman_art.stages[lives])
        print(display)
        print(f"{''.join(display)}")
    print("You win!")

def p4():
    macro.moduleStart("5")
    chosen_word = random.choice(hangman_words.word_list)
    print(f'Pssst, the solution is {chosen_word}.')
    display = []
    word_length = len(chosen_word)
    for _ in range(word_length): display += "_"
    lives = 6
    print(hangman_art.logo)

    while '_' in display:
        cls()
        guess = input("Choose a letter: ").lower()
        if guess in display:
            print(f"You have already chosen this letter [{guess}]! Choose a different letter.")
            continue
        if guess not in chosen_word:
            lives -= 1
            print(f"You chose a letter not in the word.! You lose a life.")
            if lives == 0:
                print(hangman_art.stages[lives])
                print(display)
                print("You lose!")
                exit()
        for i in range(word_length):
            if chosen_word[i] == guess: display[i] = guess
        print(hangman_art.stages[lives])
        print(display)
    print("You win!")

start()