
# задание №1
class Contact:
    def __init__(self, name, second_name, phone_number, chosen_number=False, **kwargs):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.chosen_number = chosen_number
        self.kwargs = kwargs

    def __str__(self):
        favorite = self.chosen_number
        if not self.chosen_number:
            favorite = 'нет'

        contact = {'Имя': self.name,
                   'Фамиля': self.second_name,
                   'Телефон': self.phone_number,
                   'В избранных': favorite,
                   'Дополнительная информация': self.kwargs}

        contact_as_string = ''

        for key, value in contact.items():
            if key != 'Дополнительная информация':
                contact_as_string += f'{key}: {value}\n'
            else:
                contact_as_string += f'{key}:\n'
                if value.items():
                    for k, v in value.items():
                        contact_as_string += f'\t{k}: {v}\n'
                else:
                    contact_as_string += '\tинформация отсутствует'

        return contact_as_string


# задание №2
class PhoneBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.contacts_list = []

    # Вывод контактов из телефонной книги
    def get_all_contacts(self):
        for contact in self.contacts_list:
            print(contact)

    # Добавление нового контакта
    def add_contact(self, contact):
        self.contacts_list.append(contact)

    # Удаление контакта по номеру телефона
    def dell_contact_by_number(self, phone_number):
        for contact in self.contacts_list:
            if contact.phone_number == phone_number:
                self.contacts_list.remove(contact)

    # Поиск всех избранных номеров
    def get_favorit_numbers(self):
        for contact in self.contacts_list:
            if contact.chosen_number:
                print(f'{contact.name} {contact.second_name} : {contact.chosen_number}')

    # Поиск контакта по имени и фамилии
    def get_contact_by_full_name(self, name, second_name):
        for contact in self.contacts_list:
            if name == contact.name and second_name == contact.second_name:
                print(contact)


def main():
    alex = Contact('Alex', 'Birtch', '+79990009999',  telegram='@a.birtch',
                    email='a.birtch.cocoon.io')
    jhon = Contact('Jhon', 'Smith', '+71234567809', 'нет', telegram='@jhony', email='jhony@smith.com')
    b_oconnor = Contact('Paul', 'Wolker', '+xxxxxxxxx', '71234567809' )

    myBook = PhoneBook('My PhoneBook')
    myBook.add_contact(jhon)
    myBook.add_contact(alex)
    myBook.add_contact(b_oconnor)

    print(f'\nВывод всех контактов в телефонной книге "{myBook.book_name}":')
    myBook.get_all_contacts()

    print('\nизбранные номера:')
    myBook.get_favorit_numbers()

    print('\nпоиск контакта по имени "Jhon Smith":')
    myBook.get_contact_by_full_name('Jhon', 'Smith')

    print('\nудаление контакта "Jhon Smith" по номеру телефона и вывод обновленного списка всех контактов:')
    myBook.dell_contact_by_number('+71234567809')
    myBook.get_all_contacts()

if __name__ == '__main__':
    main()
