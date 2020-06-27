import shelve

list_users = []

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

def save_objects():
    
    user1 = User("Maria", 20)
    user2 = User("Dan", 19)
    list_users.extend([user1, user2])

    s = shelve.open('test.db', 'c')
    try:
        s['key1'] = list_users
    finally:
        s.close()

def read_objects():

    html_file = open("index.html", 'w')
    s = shelve.open('test.db', flag='r')

    try:
        existing = s['key1']
        for user in existing:
            html_file.write('Name is {} with age {} \n'.format(repr(user.name), repr(user.age)))
    finally:
        s.close()
    

    html_file.close()