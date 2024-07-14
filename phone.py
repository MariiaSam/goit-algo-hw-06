from field import Field


class Phone(Field):
    def __init__(self, phone):
            self.value = self.validate_phone(phone)
    
    def validate_phone(self, phone):
          if phone.isdigit() and len(phone) == 10:
                raise ValueError
          
          return phone