class Contact:
    def __init__(self, surname, first_name, number):
        self.surname = surname
        self.first_name = first_name
        self.number = number


def deserialize_contact(contact):
    deserialized_contact = {'nom': contact.surname, 'prenom': contact.first_name, 'numero': contact.number}
    return deserialized_contact

# Inutile?
# def serialize_contact(contact):
#    serialized_contact = Contact(surname=contact['nom'], first_name=contact['prenom'], number=contact['numero'])
#    return serialized_contact

# def to_json(self):
#    import json
#    return json.loads(json.dumps(self, default=lambda o: o.__dict__))
