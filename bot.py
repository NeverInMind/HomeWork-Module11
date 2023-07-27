from types import GeneratorType

from classes import AddressBook, Name, Phone, Record

MEMORY = AddressBook()


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
        except ValueError as e:
            return e

    return wrapper


@decorator_function
def hello(val):
    val = 'How can I help you?'
    return val


@decorator_function
def add(val):
    str_to_obj = val.split(' ')
    # if str_to_obj[0] in MEMORY:
    #     return 'Name already in Contacts'
    name = Name(str_to_obj[0])
    phone = Phone(str_to_obj[1])
    rec = MEMORY.get(name.value)
    if rec:
        return rec.add_phone(phone)
        # test_obj = {str_to_obj[0]: str_to_obj[1]}
    return MEMORY.add_record(Record(name, phone))
    # return 'New contact added'


@decorator_function
def change(val):
    str_to_obj = val.split(' ')
    MEMORY[str_to_obj[0]] = str_to_obj[1]
    return 'Contact was change'


@decorator_function
def show_all(val):
    try:
        rec_per_page = int(val)
        for page in MEMORY.iterator(rec_per_page):
            yield page
    except ValueError:
        yield MEMORY


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


def parser(user_input):
    for command, kw in COMMANDS_KEYWORDS.items():
        for w in kw:
            if user_input.startswith(w):
                result = handler(command)
                user_str = user_input.replace(f'{w} ', '').strip()
                return result, user_str
    return None, None


def main():
    checker = True
    while checker is True:
        inp = input('Enter command: ')
        result, user_str = parser(inp)
        res = result(user_str)
        if isinstance(res, GeneratorType):
            for r in res:
                print(r)
                input("Press any key to continue")
        else:
            print(res)
        if res == 'Good bye!':
            checker = False


if __name__ == '__main__':
    main()
