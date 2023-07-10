from collections import UserDict
    
class Record():
    def add(*args):
        name = Name(args[0])
        phone = Phone(args[1])
        rec = Record(name, phone)
        return AddressBook.add_record(rec)

    def edit(*args):
        name = args[0]
        phone = args[1]
        rec = AddressBook.data.get(name)
        if rec:
            rec['phone'] = phone
            return rec


    def delete(*args):
        name = args[0]
        rec = AddressBook.data.get(name)
        del rec

class Field():
    pass

class Name(Field):
    pass

class Phone(Field):
    pass

class AddressBook(UserDict):
    def add_record(self, rec:Record):
        self.data[rec.value.name] = rec


ab = AddressBook()
name = Name("Bill")
phone = Phone("123456")
rec = Record(name, phone)
ab.add_record(rec)
print(ab)