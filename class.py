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
    

    def add_phone(self, phone:Phone=None):
        self.phones.append(phone)

    def edit_phone(self, old_phone:Phone=None, new_phone:Phone=None):
        try:
            search_ind = self.phones.index(old_phone)
            if search_ind != -1:
                self.phones[search_ind] = new_phone
        except ValueError:
            print(f"{old_phone} wasn't found")

    def delete_phone(self, phone:Phone=None):
        self.phones.remove(phone)


        
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
rec.delete_phone(phone2)
print(rec)