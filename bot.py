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

MEMORY = {}


def decorator_function(func):
    def wrapper(val):
        try:
            test = func(val)
            return test
        except KeyError:
            print('Invalid command')
        except IndexError:
            print('Not enough arguments')
        except UnboundLocalError:
            print('Invalid command')

    return wrapper


@decorator_function
def hello(val):
    val = 'How can I help you?'
    return val


@decorator_function
def add(val):
    str_to_obj = val.split(' ')
    if str_to_obj[0] in MEMORY:
        return 'Name already in Contacts'
    test_obj = {str_to_obj[0]: str_to_obj[1]}
    MEMORY.update(test_obj)
    return 'New contact added'


@decorator_function
def change(val):
    str_to_obj = val.split(' ')
    MEMORY[str_to_obj[0]] = str_to_obj[1]
    return 'Contact was change'


@decorator_function
def show_all(self):
    return MEMORY


@decorator_function
def show(val):
    str_to_obj = val.split(' ')
    return MEMORY[str_to_obj[0]]


@decorator_function
def close(val):
    return 'Good bye!'


COMMANDS = {'hello': hello,
            'add': add,
            'change': change,
            'phone': show,
            'show_all': show_all,
            'close': close

            }

COMMANDS_KEYWORDS = {'hello': ['hello',  'hi'],
                     'add': ['add'],
                     'change': ['change'],
                     'phone': ['phone', 'phone number'],
                     'show_all': ['show all', 'show'],
                     'close': ['good bye', 'close', 'exit']
                     }


def handler(operator):
    return COMMANDS[operator]


def main():
    checker = True
    while checker is True:
        inp = input('Enter command: ')
        for command, kw in COMMANDS_KEYWORDS.items():
            for w in kw:
                if inp.startswith(w):
                    result = handler(command)
                    user_str = inp.replace(f'{w} ', '').strip()
        res = result(user_str)
        print(res)
        if res == 'Good bye!':
            checker = False


if __name__ == '__main__':
    main()
