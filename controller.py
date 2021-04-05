from tinydb import TinyDB
from view import View
import model
from model import Contact

# contacts_table = db.table('contacts')


class Controller:
    def __init__(self):
        self.view = View()
        self.db = TinyDB('database.json')

    def create_contact(self):
        surname = self.view.input_surname()
        first_name = self.view.input_first_name()
        number = self.view.input_number()
        contact = Contact(surname, first_name, number)
        print(contact.surname, contact.first_name, contact.number)
        return contact

    def main_loop(self):
        while True:
            main_selection = self.view.display_main_menu()

            if main_selection == '1':
                self.db.table('contacts').insert(model.deserialize_contact(self.create_contact()))
                self.main_loop()

            elif main_selection == '2':
                self.delete_loop()

            elif main_selection == '3':
                self.search_loop()

            elif main_selection == '4':
                break

            else:
                self.view.display_main_menu_options()
                self.main_loop()

    def delete_loop(self):
        loop = True
        while loop:
            delete_selection = self.view.display_delete_menu()

            if delete_selection == '1':
                search = self.view.display_search_by_surname()

                confirm = input('Confirmer la suppression? (Y/N): ')
                cond = True
                while cond:
                    if confirm == 'Y':
                        self.db.table('contacts').remove(search)
                        cond = False
                    elif confirm == 'N':
                        cond = False
                    else:
                        confirm = input('Confirmer la suppression? (Y/N): ')

            elif delete_selection == '2':
                search = self.view.display_search_by_first_name()

                confirm = input('Confirmer la suppression? (Y/N): ')
                cond = True
                while cond:
                    if confirm == 'Y':
                        self.db.table('contacts').remove(search)
                        cond = False
                    elif confirm == 'N':
                        cond = False
                    else:
                        confirm = input('Confirmer la suppression? (Y/N): ')

            elif delete_selection == '3':
                break

            else:
                self.view.display_delete_menu_options()
                break

    def search_loop(self):

        while True:
            search_selection = self.view.display_search_menu()

            if search_selection == '1':
                self.view.display_search_by_surname()
                self.search_loop()

            elif search_selection == '2':
                self.view.display_search_by_first_name()
                self.search_loop()

            elif search_selection == '3':
                self.view.display_search_by_number()
                self.search_loop()

            elif search_selection == '4':
                break

            else:
                self.view.display_search_menu_options()
                self.search_loop()
