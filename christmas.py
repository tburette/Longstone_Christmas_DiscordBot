import global_data
from user import User
from os import path
import pickle


def indexOfChristmas(year: int) -> int:
    index = 0
    for c in global_data.Christmas:
        if c.getYear() == year:
            return index
    return -1


def newChristmas(year: int):
    if indexOfChristmas(year) != -1:
        return f"Noël {year} a déjà été créé!\nTu peux voir le status en tapant la commande '$noel_info' suivi de l'année qui t'intéresse"

    global_data.Christmas.append(Christmas(year))
    global_data.saveChristmas()
    return f"Noël {year} a été créé avec succès.\n Tu peux voir le status en tapant la commande '$noel_info {year}'"


def registre(user: User, year: int):
    if indexOfChristmas(year) == -1:
        return f"Noël {year} n'existe pas"
    if user == None:
        return f"Je ne te connais pas! Dis moi ton nom avec la commande $je_suis suivi de ton nom"
    ch = global_data.Christmas[indexOfChristmas(year)]
    if ch.registrationIsOpen():
        for u in ch.getRegistredUsers():
            if u.getUserName() == user.getUserName():
                return f"Merci {user.getName()}, mais tu es déjà inscrit pour Noël {ch.getYear()}"
        ch.setRegistration(user)
        global_data.Christmas[indexOfChristmas(year)] = ch
        global_data.saveChristmas()
        return f"Merci {user.getName()}, tu es bien inscrit pour Noël {ch.getYear()}"
    return f"Désolé {user.getName()}, les inscription pour Noël {ch.getYear()} sont actuellement fermées"

def openRegistration(year: int):
    if indexOfChristmas(year) == -1:
        return f"Noël {year} n'existe pas"
    ch = global_data.Christmas[indexOfChristmas(year)]
    if ch.registrationIsOpen():
        return f"Les inscriptions pour noël {year} sont déjà ouvertes"
    ch.openRegistration()
    global_data.Christmas[indexOfChristmas(year)] = ch
    global_data.saveChristmas()
    return f"Les inscriptions pour noël {year} sont maintenant ouvertes ! Feu gaz les inscriptions !!!"

def closeRegistration(year: int):
    if indexOfChristmas(year) == -1:
        return f"Noël {year} n'existe pas"
    ch = global_data.Christmas[indexOfChristmas(year)]
    if not ch.registrationIsOpen():
        return f"Les inscriptions pour noël {year} sont déjà fermées"
    ch.closeRegistration()
    global_data.Christmas[indexOfChristmas(year)] = ch
    global_data.saveChristmas()
    return f"Les inscriptions pour noël {year} sont maintenant fermées ! Finito les inscriptions !!!"


class Christmas:
    def __init__(self, year: int):
        self.__year = year
        self.__registred_users = []
        self.__pair = []
        self.__registration_is_open = False

    def getRegistredUsers(self):
        return self.__registred_users

    def setRegistration(self, user: User):
        self.__registred_users.append(user)

    def stringRegistredUsers(self):
        s = f"Les personnes inscrites pour Noël {self.getYear()} sont:\n"
        if not len(self.getRegistredUsers()):
            s += "\tAucune inscription"
            return s
        for u in self.getRegistredUsers():
            s += f"\t- {u.getName()}\n"
        return s

    def registrationIsOpen(self):
        return self.__registration_is_open

    def openRegistration(self):
        self.__registration_is_open = True
        return f"Les inscription pour Noël {self.__year} sont ouvertes"

    def closeRegistration(self):
        self.__registration_is_open = False
        return f"Les inscription pour Noël {self.__year} sont ouvertes"

    def getYear(self):
        return self.__year

    def info(self):
        s = f"Noël {self.getYear()}\n---------\n"
        registration = "fermées"
        if self.registrationIsOpen():
            registration = "ouvertes"
        s += f"Les inscriptions sont {registration}\n"
        s += self.stringRegistredUsers()
        return s