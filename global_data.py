
from user import User
from sys import getsizeof
import pickle
import os.path

usersFile = 'users.bin'
Users = []
pairsFile = 'pair.bin'
Pairs = []
christmasFile = 'christmas.bin'
Christmas = []


def saveBinaryFile(path: str, datas):

    print(f"Saving file {path}")
    file = open(path, 'wb')
    pickle.dump(datas, file)
    file.close()
    print(f"Saving file {path} - done", end="\r")


def saveUsers():
    saveBinaryFile(usersFile, Users)


def saveChristmas():
    saveBinaryFile(christmasFile, Christmas)


def loadBinaryFile(path: str):
    if not os.path.exists(path):
        print(f"File {path} doesn't exists")
        return []
    file = open(path, 'rb')
    if file.read() == b'':
        file.close()
        print(f"Nothing to read in {path}")
        return []
    file.seek(0)
    destination = pickle.load(file)
    file.close()
    print(f'Done reading datas in {path}')
    return destination


def loadUsers():
    global Users
    Users = loadBinaryFile(usersFile)


def loadChristmas():
    global Christmas
    Christmas = loadBinaryFile(christmasFile)


def load_data():
    loadUsers()
    loadChristmas()

