# Copyright (C) Baylor Projects 2024 - All Rights Reserved - DO NOT DISTRIBUTE!
# Unauthorized distribution of this file, via any medium is strictly prohibited
# Written by Baylor
# COPYLEFT POLICY: Copying is authorized without consent. ALL DERIVATIVES MUST MAINTAIN THE SAME COPYRIGHT! Patent use is prohibited.
print('\n\nCopyright (C) Baylor Projects - All Rights Reserved - DO NOT DISTRIBUTE!\n')

# Import libraries
import phonebook
pb = phonebook

# Define settings
area = None
pbx = False
countryCode = 1

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
        break

def setPbx():
    global pbx
    if pbx == False: pbx = True
    if pbx == True: pbx = False

def settings():
    while True:
        print(f'Area Code: {area}')
        print(f'PBX Mode: {pbx}')
        print('\nTo change a setting, type the first letter of it. To exit, type \'x\'')
        match input('Change setting: ').lower:
            case 'a': setArea()
            case 'p': setPbx()
            case 'x': break

# Check area code defined
if area == None: setArea()

# Main script
while True:
    print('Options:\nCall (c)\nPhonebook (p)\nSettings (s)\nExit (x)')
    match input('Choice: \n').lower:
        case 'c': call()
        case 'p': pb.run()
        case 's': settings()
        case 'x': exit()
        case _: print('Please input a valid choice.\n')