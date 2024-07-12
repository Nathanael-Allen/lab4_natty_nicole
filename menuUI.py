def print_menu(menu):  # Nathanael's module
    print('-' * 10)
    print('MENU')
    print('-' * 10)

    for i in range(0, len(menu)):
        print(f'({i + 1}) {menu[i]}')
