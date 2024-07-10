from valid import valid_string
from pathlib import Path

class ShoppingList:
    def __init__(self):
        self.myList = ['test_1', 'test_2', 'test_3']

    def printList(self):
        '''
        Needs to check if list is empty and if not print out each
        item of the list on a new line
        '''
        pass

    def addItem(self):
        # Needs to take a string value as input and append it to the list
        pass

    def removeItem(self, option=int):
        # Needs to take the option/index as an argument and pop it from the list.
        pass

    def saveList(self):
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


        
