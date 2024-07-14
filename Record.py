from name import Name
from phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self):
        pass

    def remove_phone(self):
        pass

    def edit_phone(self):
        pass

    def find_phone(self):
        pass
