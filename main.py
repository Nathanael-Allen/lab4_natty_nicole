# Authors: Nathanael Allen, Nicole Sausville
# Assignment: Lab 4
# Date: 07/10/24
# Description: This menu driven program allows a user to create and edit a shopping list as well as 
# save it to the file system as a text file

# Contributions: main.py, shoppingList.py, and valid.py were a collaboration between the two of us
# each of us contributing about 50% of each file, Nathanael added menuUI module and Nicole added sorting.py.

from valid import *
from menuUI import *
from shoppingList import ShoppingList
import sorting

# A list of strings containing categories for the main menu
MAIN_MENU = [
    'Add Item',  # Option 1
    'Remove Item',  # Option 2
    'Print List',  # Option 3
    'Sort List',  # Option 4
    'Save List',  # Option 5
    'QUIT'  # Option 6
]


def main():
    my_shopping_list = ShoppingList()
    print('SHOPPING LIST')
    while True:
        print()
        print_menu(MAIN_MENU)
        option = valid_option(MAIN_MENU)

# This will be a switch statement that acts as our menu
        match option:
            case 1:
                print('\nAdd item')
                my_shopping_list.add_item()
            case 2:
                if len(my_shopping_list.myList) > 0:
                    print('\nRemove item')
                    my_shopping_list.remove_item()
                else:
                    print('List is empty...')
            case 3:
                print()
                my_shopping_list.display_list()
                if(enter_key('\nPress enter for main menu...')):
                    continue
            case 4:
                print('\nList Sorted')
                my_shopping_list.sort_list()

            case 5:
                if(len(my_shopping_list.myList) > 0):
                    my_shopping_list.save_list()
                else:
                    print('List empty nothing to save...')
            case 6:
                print('\nProgram exiting...')
                break
        



if __name__ == '__main__':
    main()