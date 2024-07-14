from field import Field


class Phone(Field):

    def __init__(self, phone):
        self.value = self.validate_phone(phone)

    def validate_phone(self, phone):

        if not phone.isdigit():
            raise ValueError("Phone number must contains isdigit")

        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")

        return phone
