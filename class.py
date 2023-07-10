from collections import UserDict

class Field():
    pass

class Name():
    def __init__(self, name) -> None:
        self.name = name

class Phone():
    def __init__(self, phone) -> None:
        self.phone = phone
    
class Record():
    def __init__(self, *args) -> None:
        self.name = args[0].name
        self.phone = args[1].phone

        

class AddressBook(UserDict):
    
    def add_record(self, rec:Record):
        self.data[rec.name] = rec.phone


ab = AddressBook()
name = Name("Bill")
phone = Phone("123456")
rec = Record(name, phone)
ab.add_record(rec)
print(ab)