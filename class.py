from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value


class Name(Field):
    ...


class Phone(Field):
    ...
    
    
class Record():
    def __init__(self, name:Name, phone:Phone=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def __str__(self) -> str:
        return f"{self.name} : {', '.join(str(p) for p in self.phones)}"

        
class AddressBook(UserDict):
    
    def add_record(self, rec:Record):
        self.data[rec.name] = rec
    
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.values())


ab = AddressBook()
name = Name("Bill")
phone = Phone("123456")
phone2 = Phone('31452')
phone3 = Phone('45641')
rec = Record(name, phone)
rec.add_phone(phone2)
rec.edit_phone(phone3, phone2)
print(rec)