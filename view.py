from tinydb import TinyDB, Query
db = TinyDB('database.json')
contacts_table = db.table('contacts')


class View:
    def __init__(self):
        pass

    def display_main_menu(self):
        main_menu = dict()
        main_menu['1'] = 'Créer un contact'
        main_menu['2'] = 'Supprimer un contact'
        main_menu['3'] = 'Rechercher un contact'
        main_menu['4'] = 'Quitter le programme'

        options = main_menu.keys()
        print('\n***********************************************\nMENU PRINCIPAL:')
        for entry in options:
            print(entry, main_menu[entry])

        main_selection = input('***********************************************\nChoisissez une option: ')
        return main_selection

    def display_main_menu_options(self):
        print('\n***********************************************\nVeuillez choisir une option entre 1 et 4')

    def display_delete_menu(self):

        delete_menu = dict()
        delete_menu['1'] = 'Rechercher par nom'
        delete_menu['2'] = 'Rechercher par prenom'
        delete_menu['3'] = 'Menu principal'

        options = delete_menu.keys()
        print('\n***********************************************\nMENU SUPPRESSION:')
        for entry in options:
            print(entry, delete_menu[entry])
        delete_selection = input('***********************************************\nChoisissez une option: ')
        return delete_selection

    def display_delete_menu_options(self):
        print('\n***********************************************\nVeuillez choisir une option entre 1 et 3')

    def display_search_menu(self):
        search_menu = dict()
        search_menu['1'] = 'Rechercher par nom'
        search_menu['2'] = 'Rechercher par prenom'
        search_menu['3'] = 'Annuaire inverse'
        search_menu['4'] = 'Menu principal'

        options = search_menu.keys()
        print('\n***********************************************\nMENU RECHERCHE:')
        for entry in options:
            print(entry, search_menu[entry])
        search_selection = input('***********************************************\nChoisissez une option: ')
        return search_selection

    def display_search_menu_options(self):
        print('\n***********************************************\nVeuillez choisir une option entre 1 et 4')

    def display_search_by_surname(self):
        surname = self.input_surname()
        s = Query()
        print(contacts_table.search(s.nom == surname))
        result = (s.nom == surname)
        return result

    def display_search_by_first_name(self):
        first_name = self.input_first_name()
        s = Query()
        print(contacts_table.search(s.prenom == first_name))
        result = (s.prenom == first_name)
        return result

    def display_search_by_number(self):
        number = self.input_number()
        s = Query()
        print(contacts_table.search(s.numero == number))

    def input_surname(self):
        surname = input('Veuillez entrer le nom de famille: ')
        return surname

    def input_first_name(self):
        first_name = input('Veuillez entrer le prénom: ')
        return first_name

    def input_number(self):
        number = input('Veuillez entrer le numéro de téléphone: ')
        return number
