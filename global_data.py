
from user import User
from sys import getsizeof
import pickle
import os.path

usersFile = 'users.bin'
Users = []


def saveUsers():

    print("Saving users")
    file = open(usersFile, 'wb')
    pickle.dump(Users, file)
    file.close()
    print("Saving users - done", end="\r")


def loadUsers():
    global Users
    if not os.path.exists(usersFile):
        print("Zero file to read")
        return
    file = open(usersFile, 'rb')
    if file.read() == b'':
        file.close()
        print("Nothing to read")
        return
    file.seek(0)
    Users = pickle.load(file)
    file.close()
    print('Done reading the list')
    print(Users)


def load_data():
    loadUsers()

