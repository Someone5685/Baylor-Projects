# Core
area = 205
phb = {
    'Operator': 0,
    'Weather': int(str(area)+str(3906215))
    }
# Define functions
def areaIs(prelimArea):
    global area
    area = prelimArea
def revSrc(num):
    for key, value in phb.items():
        if value == num:
            return key

def add():
    while True:
        newName = input('Name: ')
        if len(newName) >= 30:
            print('Name is too long.')
            continue
        break
    while True:
        try: newNum = int(input('Number (Excluding area code): '))
        except ValueError:
            print('Please input a valid number')
            continue
        if len(str(newNum)) != 7:
            print('Please input exactly 7 digits')
            continue
        break
    print()
    phb[newName]=int(str(area)+str(newNum))

def rem():
    remKey = input('Remove: ')
    del phb[remKey]

def src():
    srcKey = input('Search: ')
    print(phb[srcKey])

def prn(): print(phb)

def clr():
    global phb
    phb = {
        'Operator': 0,
        'Weather': area+3906215
        }

# Main script
def run():
    print('\n\nPHONEBOOK')
    while True:
        input('Press \'Enter\' to continue.\n')
        print('Options:\nAdd (a)\nRemove (r)\nSearch (s)\nPrint (p)\nClear (c)\nExit (x)\n')
        match input('Action: ').lower():
            case 'a': add()
            case 'r': rem()
            case 's': src()
            case 'p': prn()
            case 'c': clr()
            case 'x': break
            case _: print('Please input a valid option.')