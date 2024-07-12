from valid import valid_string, valid_int
from pathlib import Path
from sorting import sort_list

class ShoppingList:
    def __init__(self):  # Nathanael's function
        self.myList = []

    def sort_list(self):  # Nicole's function
        return sort_list(self.myList)

    def display_list(self):  # Nicole's function
        if len(self.myList) == 0:
            # If there is nothing in your list, tell the user that it's empty.
            print('No items in your list!')
            return
        else:
            # Otherwise, print the list out on separate lines.
            for number, item in enumerate(self.myList):
                print(f'{number + 1}: {item}')  # + 1 added to visually start list at number 1 instead of 0.


    def add_item(self):  # Nicole's function
        # Needs to take a string value as input and append it to the list
        user_input = valid_string('Add an item: ')
        self.myList.append(user_input)

    def remove_item(self, option=int): # Nicole's function
        # Needs to take the option/index as an argument and pop it from the list.
        self.display_list()
        item_number_to_remove = valid_int("Enter item number to remove item: ")
        # -1 added to compensate for 1 added in the add_item function to visually start list number at 1
        del self.myList[item_number_to_remove - 1]
        print()
        print("Updated List:")
        self.display_list()

    def save_list(self):  # Nathanael's function
        listName = valid_string('Name your list: ') + '.txt'
        listPath = Path().joinpath(Path().resolve(), 'lists', listName)
        try:
            file = open(listPath, 'x')
            file.close()
        except(Exception):
            print('File already exists...')
            return
        
        file = open(f'{listPath}', 'a')
        for item in self.myList:
            file.write(f'{item}\n')
        file.close()
        print(f'List saved to: {listPath}')


        
