from collections import UserDict
from record import Record

class AddressBook(UserDict):

    def add_record(self, record: Record):
        name = record.name.value
        if name in self.data:
            existing_record = self.data[name]
            for phone in record.phones:
                existing_record.add_phone(phone.value)
            print(f"Record with name {name} already exists. Phones updated.")
        else:
            self.data[name] = record


    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name not in self.data:
           print(f"Record with name {name} not found.")
        else:
          del self.data[name]
