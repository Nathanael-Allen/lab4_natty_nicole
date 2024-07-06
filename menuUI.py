def printMenu(menu):
    print('-' * 10)
    print('MENU')
    print('-' * 10)

    for i in range(0, len(menu)):
        print(f'({i + 1}) {menu[i]}')

