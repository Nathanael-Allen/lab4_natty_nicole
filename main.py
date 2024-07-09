from valid import *
from menuUI import *
from shoppingList import ShoppingList


MAIN_MENU = [
    'Add Item', # Option 1
    'Remove Item', # Option 2
    'Print List', # Option 3
    'Save List', # Option 4 
    'QUIT' # Option 5
]


def main():
    shoppingList = ShoppingList()
    print('SHOPPING LIST')
    while True:
        printMenu(MAIN_MENU)
        option = validOption(MAIN_MENU)

        match option:
            case 1:
                print('Add item')
            case 2:
                print('Remove item')                    
            case 3:
                shoppingList.printList()
                if(not enterKey('\nEnter for main menu or type "exit" to close program: ')):
                    print('Program exiting...')
                    break
            case 4:
                if(len(shoppingList.myList) > 0):
                    shoppingList.saveList()
                else:
                    print('List empty nothing to save...')
            case 5:
                print('Program exiting...')
                break
        



if __name__ == '__main__':
    main()