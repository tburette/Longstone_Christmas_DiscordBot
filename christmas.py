import datetime
import random
from itertools import permutations, combinations
from random import shuffle
import global_data
import user
from user import User
from os import path
import pickle

def randomFloat():
    rnd = random.SystemRandom().randint(0, 99) / float(100)
    return rnd


def randomList(list: list):
    rand_list = list.copy()
    random.shuffle(rand_list, randomFloat)
    return rand_list


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

def unregistre(user: User, year: int):
    if indexOfChristmas(year) == -1:
        return f"Noël {year} n'existe pas"
    if user == None:
        return f"Je ne te connais pas! Dis moi ton nom avec la commande $je_suis suivi de ton nom"
    ch = global_data.Christmas[indexOfChristmas(year)]
    if ch.registrationIsOpen():
        for u in ch.getRegistredUsers():
            if u.getUserName() == user.getUserName():
                ch.removeRegistration(user)
                global_data.Christmas[indexOfChristmas(year)] = ch
                global_data.saveChristmas()
                return f"Merci {user.getName()}, ton inscription pour Noël {ch.getYear()} a été retirée. <3 bisou"

        return f"Tu n'es pas inscrit à noel {ch.getYear()}, je ne peux pas retirer ton inscription"
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


def isSame(couple):
    first = couple[0]
    second = couple[1]
    return first == second


def isCouple(couple):
    first = couple[0]
    second = couple[1]
    if first.getPartner() == second:
        return True
    return False


class Christmas:
    def __init__(self, year: int):
        self.__year = year
        self.__registred_users = global_data.Users# [] #TODO retirer le commentaire quand les test seront OK
        self.__pair = []
        self.__pair_is_already_created = False
        self.__registration_is_open = False

    def getRegistredUsers(self):
        return self.__registred_users

    def setRegistration(self, user: User):
        self.__registred_users.append(user)

    def removeRegistration(self, TheUser: User):
        index = -1
        for i in range(0, len(self.__registred_users)):
            if self.__registred_users[i].getUserName() == TheUser.getUserName():
                index = i
        if index != -1:
            del self.__registred_users[index]
        print("removed ok")

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

    def pairIsAlreadyCreated(self):
        return self.__pair_is_already_created

    def resetPairs(self):
        self.__pair_is_already_created = False
        self.__pair = []
    def createPairs(self):
        if self.__pair_is_already_created:
            return self.__pair

        if self.registrationIsOpen():
            return self.__pair
        MAX_ATTEMPS = 2000
        attempts = 0
        pair = []
        find_composition = False
        sender = self.getRegistredUsers().copy()
        receiver = self.getRegistredUsers().copy()
        sender = randomList(sender)
        receiver = randomList(receiver)
        while not find_composition and attempts < MAX_ATTEMPS:
            for i in range(0, len(self.getRegistredUsers())):
                pair.append((sender[i], receiver[i]))
                is_couple = isCouple(pair[i])
                is_already_couple_in_christmas = self.isAlreadyCoupleInChristmas(pair[i])
                is_same = isSame(pair[i])
                if is_couple or is_already_couple_in_christmas or is_same:
                    find_composition = False
                    attempts += 1
                    print(f"Tentative: {attempts}")
                    sender = randomList(sender)
                    receiver = randomList(receiver)
                    pair = []
                    break
                find_composition = True
        self.__pair = pair
        self.__pair_is_already_created = True
        return self.__pair

    def getPairs(self) -> list:
        return self.__pair

    def isAlreadyCoupleInChristmas(self, couple):
       for ch in global_data.Christmas:
           if ch != self:
               for c in ch.getPairs():
                   if c == couple:
                       return True
       return False





