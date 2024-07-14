from addressBook import AddressBook
from record import Record

if __name__ == "__main__":

# Створення нової адресної книги
    book = AddressBook()
    print(book)

    # Створення запису для John
    john_record = Record("John")
    print(john_record)

    john_record.add_phone("1234567890")
    print(john_record)

    john_record.add_phone("5555555555")
    print(john_record)

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print(book)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    print(jane_record)

    jane_record.add_phone("9876543210")
    print(jane_record)

    book.add_record(jane_record)
    print('book:', book)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
