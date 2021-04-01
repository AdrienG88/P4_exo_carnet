class View:
    def __init__(self):
        pass


    def display_menu(self):
        from controller import Controller
        c = Controller()
        Controller.main_loop(c)

    # Les fonctions de la vue ne doivent-elles pas rien retourner?

    def input_surname(self):
        surname = input('Veuillez entrer le nom de famille: ')
        return surname

    def input_first_name(self):
        first_name = input('Veuillez entrer le prénom: ')
        return first_name

    def input_number(self):
        number = input('Veuillez entrer le numéro de téléphone: ')
        return number
