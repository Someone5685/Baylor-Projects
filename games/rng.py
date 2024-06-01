# rng.py, The RNG guessing game.

# Copyright (C) Baylor Projects 2024 - All Rights Reserved - DO NOT DISTRIBUTE!
# Unauthorized distribution of this file, via any medium is strictly prohibited
# Written by Baylor
# COPYLEFT POLICY: Copying is authorized without consent. ALL DERIVATIVES MUST MAINTAIN THE SAME COPYRIGHT! Patent use is prohibited.
print('\n\nCopyright (C) Baylor Projects - All Rights Reserved - DO NOT DISTRIBUTE!\n')

from random import randint
while True:
    print('Welcome to the RNG guessing game.')
    try:
        range = int(input('range of numbers to guess: 1-'))
        tries = int(input('Number of tries you will get: '))
        trycount = 0
    except ValueError:
            print('Please input an integer.')
            continue
    break
num = randint(1,range)
num = 5
print(f'I\'m thinking of a number between 1 and {range}. Try to guess it.')
while tries != 0:
    while True:
        try: plr = int(input('Guess: '))
        except ValueError: 
            print('Please input an integer.')
            continue
        break
    trycount+1
    if plr == num:
        print(f'Congratulations! You guessed my number in {trycount} tries!\nPress \'Enter\' to exit.')
        input()
        exit()