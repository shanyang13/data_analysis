def message():
    name = 'Eric'
    print(f"Hello {name}, would you like to learn some Python today?")


def up_and_down():
    name = 'Albert Einstein'
    print(f'{name} once said,"A person who never made a mistake never tried anything new."')
    print(f'{name.upper()} once said,"A person who never made a mistake never tried anything new."')
    print(f'{name.lower()} once said,"A person who never made a mistake never tried anything new."')


def list_base():
    list1 = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']
    print(list1)
    list1.insert(2, 'namex')
    print(list1)
    del list1[2]
    print(list1)
    list1.pop()
    print(list1)
    a = list1.pop()
    print("list:", list1)
    print("a:", a)
    b = list1.pop(-2)
    print("list:", list1)
    print("b:", b)
    list1.remove('name1')
    print("list:", list1)
    delete_name = 'name3'
    list1.remove(delete_name)
    print("list:", list1)


def list_for_loop():
    list1 = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']
    for i in list1:
        print(i)

    print('---------------------------')

    for i in range(1, 5):
        print(i)

    print('---------------------------')

    for i in range(6):
        print(i)

    print('---------------------------')
    even_number = list(range(2, 11, 2))
    print(even_number)

    even_numbers = [x + 1 for x in range(1, 11) if x % 2 == 0]
    print(even_numbers)
    even_numbers = [x for x in range(1, 11) if x % 2 == 0]
    print(even_numbers)


def dict_base():
    dist1 = {'name': 'Tom', 'age': '18', 'point': '25'}
    for i, j in dist1.items():
        print(i)
        print(j)
        print(i, j)

    users = {
        'asinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
        },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'princeton'
        }
    }

    for username, user_info in users.items():
        print("Username:", username)
        print("full name:", user_info['first'].title(), " ", user_info['last'].title())
        print("location:", user_info['location'].title())


def input_something():
    message = input("Tell me something: ")
    print(message)


def input_dict():
    responses = {}
    polling_active = True
    while polling_active:
        name = input("What is your name? ")
        resource = input("What is your resource? ")

        responses[name] = resource

        repeat = input("Would you like to repeat? (y/n) ")
        if repeat == 'n':
            polling_active = False

    for name, resource in responses.items():
        print(f"{name}: {resource}")


if __name__ == '__main__':
    # message()
    # up_and_down()
    # list_base()
    # list_for_loop()
    # dict_base()
    # input_something()
    input_dict()
