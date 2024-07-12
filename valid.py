# Nathanael's module

def valid_float_input(question) -> float:
    while True:
        try:
            usr_input = input(question).strip()
            if not usr_input:
                raise ValueError
            if float(usr_input) < 0:
                raise ValueError
            else:
                return float(usr_input)
        except Exception:
            print('ERROR: Invalid input')


def valid_string(question) -> str:
    while True:
        try:
            usr_input = input(question).strip()
            if not usr_input:
                raise ValueError
            else:
                return usr_input
        except Exception:
            print('ERROR: Invalid input')


def valid_yn(question) -> bool:
    while True:
        try:
            usr_input = input(question).strip().lower()
            if not usr_input:
                raise ValueError
            elif usr_input == 'y' or usr_input == 'yes':
                return True
            elif usr_input == 'n' or usr_input == 'no':
                return False
            else:
                raise Exception
        except(Exception):
            print('ERROR: Invalid input')


def valid_az(question) -> str:
    while True:
        try:
            usr_input = input(question).strip().lower()
            if not usr_input:
                raise ValueError
            elif usr_input == 'a' or usr_input == 'z':
                return usr_input
            else:
                raise Exception
        except(Exception):
            print("ERROR: Please either enter an 'A' or 'Z'")


def valid_int(question='Input valid integer: '):
    while True:
        try:
            usr_input = input(question).strip()
            if not usr_input:
                raise ValueError
            if int(usr_input) < 0:
                raise ValueError
            else:
                return int(usr_input)
        except(Exception):
            print('ERROR: Not a valid Input')


def valid_option(a_list, question='Select option: '):
    """
    Takes the menu list as first argument and input prompt as second argument.
    Needs to check if user input is A: a positive integer greater than 0
    and B: Is not greater than the length of the list
    """
    while True:
        try:
            usr_input = int(input(question).strip())
            if not usr_input:
                raise ValueError
            if usr_input < 1 or usr_input > len(a_list):
                print('ERROR: Option not in list')
            else:
                return usr_input
        except(Exception):
            print('ERROR: Not a valid Input')


def enter_key(question='Press enter'):
    while True:
        try:
            usr_input = input(question).lower().strip()
            if usr_input == '':
                return True
            else:
                continue
        except(Exception):
            continue
        