def validFloatInput(question) -> float:
    while True:
        try:
            usrInput = input(question).strip()
            if(not usrInput):
                raise ValueError
            if(float(usrInput) < 0):
                raise ValueError
            else:
                return float(usrInput)
        except(Exception):
            print('ERROR: Invalid input')


def validString(question) -> str:
    while True:    
        try:
            usrInput = input(question).strip()
            if(not usrInput):
                raise ValueError
            else:
                return usrInput
        except(Exception):
            print('ERROR: Invalid input')


def validYN(question) -> bool:
    while True:
        try:
            usrInput = input(question).strip().lower()
            if(not usrInput):
                raise ValueError
            elif(usrInput == 'y' or usrInput == 'yes'):
                return True
            elif(usrInput == 'n' or usrInput == 'no'):
                return False
            else:
                raise Exception
        except(Exception):
            print('ERROR: Invalid input')

def validInt(question='Input valid integer: '):
    while True:
        try:
            usrInput = input(question).strip()
            if(not usrInput):
                raise ValueError
            if(int(usrInput) < 0):
                raise ValueError
            else:
                return int(usrInput)
        except(Exception):
            print('ERROR: Not a valid Input')

def validOption(menu ,question='Select option: '):
    '''
    Takes the menu list as first argument and input prompt as second argument.
    Needs to check if user input is A: a positive integer greater than 0
    and B: Is not greater than the length of the list
    '''
    while True:
        try:    
            usrInput = int(input(question).strip())
            if(not usrInput):
                raise ValueError
            if(usrInput < 0 or usrInput > len(menu)):
                print('ERROR: Option not in list')
            else:
                return usrInput
        except(Exception):
            print('ERROR: Not a valid Input')

def enterKey(question='Press enter'):
    while True:
        try:
            usrInput = input(question).lower().strip()
            if(usrInput == ''):
                return True
            elif(usrInput == 'exit'):
                return False
            else:
                continue
        except(Exception):
            continue


        