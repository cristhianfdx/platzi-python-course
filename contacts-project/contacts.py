import csv


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self.__contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.__contacts.append(contact)
        self.__save()

    def show_all(self):
        for contact in self.__contacts:
            self.__print_contact(contact)

    def delete(self, name):
        for index, contact in enumerate(self.__contacts):
            if contact.name.lower() == name.lower():
                del self.__contacts[index]
                self.__save()
                break

    def search(self, name):
        for contact in self.__contacts:
            if contact.name.lower() == name.lower():
                self.__print_contact(contact)
                break
        else:
            self.__not_found()

    def update(self, name):
        pass

    def __not_found(self):
        print('***************')
        print('¡No encontrado!')
        print('***************')

    def __print_contact(self, contact):
        print('--- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefóno: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * ---')

    def __save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self.__contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)

        for index, row in enumerate(reader):
            if index == 0:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])


    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('comando no encontrado')


if __name__ == '__main__':
    print('B I E N V E N I D O S')
    run()
