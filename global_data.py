
from user import User
from sys import getsizeof
import pickle
import os.path
import christmas

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
    ###Valeurs de test
    # Users = [
    #     User("ByLex#0045", "Alex"),
    #     User("Cinducci", "Cindy"),
    #     User("Cacahuette", "Tony"),
    #     User("Pepito", "Juan Carlos Lopez Perreira"),
    #     User("Couscous", "Rachid"),
    #     User("Bamboula", "Paradis Désiré"),
    #     User("USNavyForEver", "Jason O'Sean"),
    #     User("Colinet", "Colin"),
    #     User("l_impaire", "l_impaire")
    # ]
    # Users[0].partner = Users[1]
    # Users[1].partner = Users[0]
    # Users[2].partner = Users[3]
    # Users[3].partner = Users[2]
    # Users[4].partner = Users[5]
    # Users[5].partner = Users[4]
    # Users[6].partner = Users[7]
    # Users[7].partner = Users[6]
    Users = loadBinaryFile(usersFile)


def loadChristmas():
    global Christmas
    ###Valeurs de test
    # c1 = christmas.Christmas(2019)
    # c2 = christmas.Christmas(2020)
    # c3 = christmas.Christmas(2021)
    # c4 = christmas.Christmas(2022)
    # Christmas = [c1, c2, c3, c4]

    Christmas = loadBinaryFile(christmasFile)


def load_data():
    loadUsers()
    loadChristmas()

