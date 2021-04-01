from controller import *

db = TinyDB('database.json')
contacts_table = db.table('contacts')

default = View()
View.display_menu(default)
