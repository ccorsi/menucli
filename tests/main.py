if __name__ == "__main__":
    from menucli import create_menu, add_menu_item_action

    menu = create_menu('Main Menu', 'Exit')


    def menu_Item():
        print('Called Menu Item Method')


    add_menu_item_action(menu, 'Menu Item', menu_Item, menu)
    menu.show()
