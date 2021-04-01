from tinydb import TinyDB, Query
from view import View
from model import Contact

db = TinyDB('database.json')
contacts_table = db.table('contacts')


class Controller:
    def __init__(self):
        pass

    def create_contact(self):
        v = View()
        surname = View.input_surname(v)
        first_name = View.input_first_name(v)
        number = View.input_number(v)
        contact = Contact(surname, first_name, number)
        print(contact.surname, contact.first_name, contact.number)
        return contact

    def main_loop(self):
        main_menu = dict()
        main_menu['1'] = 'Créer un contact'
        main_menu['2'] = 'Supprimer un contact'
        main_menu['3'] = 'Rechercher un contact'
        main_menu['4'] = 'Quitter le programme'

        while True:
            options = main_menu.keys()
            print('\n***********************************************\nMENU PRINCIPAL:')
            for entry in options:
                print(entry, main_menu[entry])

            main_selection = input('***********************************************\nChoisissez une option: ')

            if main_selection == '1':
                import model
                contacts_table.insert(model.deserialize_contact(self.create_contact()))

            if main_selection == '2':
                self.delete_loop()

            if main_selection == '3':
                self.search_loop()

            if main_selection == '4':
                break

            else:
                print('Veuillez choisir une option entre 1 et 3')

    def delete_loop(self):

        delete_menu = dict()
        delete_menu['1'] = 'Rechercher par nom'
        delete_menu['2'] = 'Rechercher par prenom'
        delete_menu['3'] = 'Menu principal'

        while True:
            options = delete_menu.keys()
            print('\n***********************************************\nMENU SUPPRESSION:')
            for entry in options:
                print(entry, delete_menu[entry])
            search_selection = input('***********************************************\nChoisissez une option: ')

            if search_selection == '1':
                # appel à la vue ne fonctionne pas
                v = View()
                surname = View.input_surname(v)
                s = Query()
                print(contacts_table.search(s.nom == surname))

                confirm = input('Confirmer la suppression? (Y/N): ')
                cond = True
                while cond:
                    if confirm == 'Y':
                        contacts_table.remove(s.nom == surname)
                        cond = False
                    elif confirm == 'N':
                        cond = False
                    else:
                        pass

            if search_selection == '2':
                v = View()
                first_name = View.input_first_name(v)
                s = Query()
                print(contacts_table.search(s.prenom == first_name))

                confirm = input('Confirmer la suppression? (Y/N): ')
                cond = True
                while cond:
                    if confirm == 'Y':
                        contacts_table.remove(s.prenom == first_name)
                        cond = False
                    elif confirm == 'N':
                        cond = False
                    else:
                        pass

            if search_selection == '3':
                break

    def search_loop(self):
        search_menu = dict()
        search_menu['1'] = 'Rechercher par nom'
        search_menu['2'] = 'Rechercher par prenom'
        search_menu['3'] = 'Annuaire inverse'
        search_menu['4'] = 'Menu principal'

        while True:
            options = search_menu.keys()
            print('\n***********************************************\nMENU RECHERCHE:')
            for entry in options:
                print(entry, search_menu[entry])
            search_selection = input('***********************************************\nChoisissez une option: ')

            if search_selection == '1':
                v = View()
                surname = View.input_surname(v)
                s = Query()
                print(contacts_table.search(s.nom == surname))

            if search_selection == '2':
                v = View()
                first_name = View.input_first_name(v)
                s = Query()
                print(contacts_table.search(s.prenom == first_name))

            if search_selection == '3':
                v = View()
                number = View.input_number(v)
                s = Query()
                print(contacts_table.search(s.numero == number))

            if search_selection == '4':
                break
