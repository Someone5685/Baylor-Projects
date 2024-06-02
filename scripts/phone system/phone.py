# Copyright (C) Baylor Projects 2024 - All Rights Reserved
# Unauthorized distribution of this file, via any medium is strictly prohibited
# Written by Baylor
# COPYLEFT POLICY: Copying is authorized without consent. Derivation, distribution, or patent use is prohibited.
print('\n\nCopyright (C) Baylor Projects - All Rights Reserved\n')

# Library operations
import phonebook
pb = phonebook
pb.areaIs(205)

# Define settings
area = 205
print(f'Your area code is {area}. This can be changed in settings.\nDefault: 205')
pbx = False

# Define functions
def setArea():
    while True:
        global area
        try: prelimArea = int(input ('Area code: '))
        except ValueError:
            print('Value must be an integer.')
            continue
        if prelimArea > 999 or prelimArea < 200:
            print('Integer must be 200-999')
            continue
        area = prelimArea
        pb.areaIs(area)
        break

def settings():
    while True:
        global pbx
        global area
        print(f'\nArea Code: {area}')
        print(f'PBX Mode (Unfinished): {pbx}')
        print('\nTo change a setting, type the first letter of it. To exit, type \'x\'')
        match input('Change setting: ').lower():
            case 'a': setArea()
            case 'p': pbx = not pbx
            case 'x': break
            case _: print('Please input a valid choice.\n')

def call():
    while True:
        try: dial = int(input('Dial: '))
        except ValueError:
            print('Please dial a valid number')
            continue
        break
    name = pb.revSrc(dial)
    print(f'\n\nHello! You\'ve called {name}.')
    input('\nPress \'Enter\' to continue')

# Main script
while True:
    print('\nOptions:\nCall (c)\nPhonebook (p)\nSettings (s)\nExit (x)')
    match input('\nAction: ').lower():
        case 'c': call()
        case 'p': pb.run()
        case 's': settings()
        case 'x': exit()
        case _: print('Please input a valid choice.\n')