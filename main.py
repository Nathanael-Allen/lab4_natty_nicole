from valid import *
from menuUI import *
from shoppingList import ShoppingList
import sorting


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
        printMenu(MAIN_MENU)
        option = valid_option(MAIN_MENU)

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
                if(not enter_key('\nEnter for main menu or type "exit" to close program: ')):
                    print('Program exiting...')
                    break
            case 4:
                print('\nList Sorted')
                my_shopping_list.sort_list()

            case 5:
                if(len(my_shopping_list.myList) > 0):
                    my_shopping_list.saveList()
                else:
                    print('List empty nothing to save...')
            case 6:
                print('\nProgram exiting...')
                break
        



if __name__ == '__main__':
    main()