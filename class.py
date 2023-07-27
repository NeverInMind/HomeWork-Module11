from collections import UserDict
from datetime import datetime
import re

class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
    
    def __str__(self) -> str:
        return self.value

class Name(Field):
    ...

class Phone(Field):
    @property
    def value(self):
        ...

    @value.setter
    def value(self, value):
        if not re.match(r'^\+38\d{10}$', value):
            raise ValueError("Phone number should be in the format +380XXXXXXXXX")
        self.__value = value

class Birthday(Field):
    @property
    def value(self):
        ...
        
    @value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, '%d-%m-%Y').date()
       
class Record():
    def __init__(self, name:Name, phone:Phone=None, birthday:Birthday=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        if birthday:
            self.bthday = birthday
    
    def __str__(self) -> str:
        return f"{self.name} : {', '.join(str(p) for p in self.phones)}, {self.bthday}"
    

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

    def days_to_birthday(self, birthday:Birthday=None):
        today = datetime.now()
        brthday = datetime(today.year, birthday.month, birthday.day)
        if today > brthday:
            brthday = (brthday.year + 1, brthday.month, brthday.day)
        return (brthday - today).days
        
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
brthday = Birthday(datetime(2023, 6, 30))
rec = Record(name, phone, brthday)
print(rec)