import christmas
import global_data
from user import User, getUserByName
#TODO stocker que les username des Users car copie problematiques....
chr21 = christmas.Christmas(2021)
chr22 = christmas.Christmas(2022)

users = [User("ByLex#0045", "Alex"), User("Vivianus#3950", "Vivien"), User("méliz#0605", "Mailys"),
         User("Romain#4956", "Romain"), User("Cricri#7570", "Cricri"), User("Cinducci#3391", "Cindy"),
         User("Lucine#2884", "Lucie"), User("Laurette#1509", "Laura"), User("S.A.M.#1938", "Gabin")]
global_data.Users = users
global_data.Users[0].setPartner("Cindy")
global_data.Users[1].setPartner("Lucie")
global_data.Christmas.append(chr21)
global_data.Christmas.append(chr22)
global_data.saveUsers()

global_data.Christmas[0].openRegistration()
for user in users:
    print(christmas.registre(user, 2021))

global_data.Christmas[1].openRegistration()
print(christmas.registre(getUserByName("Alex"), 2022))
print(christmas.registre(getUserByName("Vivien"), 2022))
print(christmas.registre(getUserByName("Mailys"), 2022))
print(christmas.registre(getUserByName("Romain"), 2022))
print(christmas.registre(getUserByName("Cricri"), 2022))
print(christmas.registre(getUserByName("Cindy"), 2022))
print(christmas.registre(getUserByName("Lucie"), 2022))
print(christmas.registre(getUserByName("Laura"), 2022))
global_data.Christmas[1].closeRegistration()


# Cricri -> Lucie
# Alex -> Vivien
# Cindy -> Cricri
# Laura ->
# Vivien ->
# Maylis -> Gabin
# Romain ->

pair = [(users[4], users[6]),  # Cricri -> Lucie
        (users[0], users[1]),  # Alex -> Vivien
        (users[5], users[4]),  # Cindy -> Cricri
        (users[7], users[5]),  # Laura -> Cindy
        (users[1], users[7]),  # Vivien -> Laura
        (users[8], users[2]),  # Gabin -> Maylis
        (users[6], users[0]),  # Lucie -> Alex
        (users[2], users[8])  # Maylis -> Gabin
        ]


global_data.Christmas[0]._Christmas__pair = pair
global_data.Christmas[0]._Christmas__pair_is_already_created = True
global_data.Christmas[0].closeRegistration()


print("2021\n")
index = christmas.indexOfChristmas(2021)
global_data.Christmas[index].printPairs()
print("2022\n")
index = christmas.indexOfChristmas(2022)
global_data.Christmas[index].closeRegistration()
global_data.Christmas[index].createPairs()
global_data.Christmas[index].printPairs()

nbCouple = 0
nbSame = 0
for i in range(0, 1000):
    global_data.Christmas[index].createPairs()

    for p in global_data.Christmas[index].getPairs():
        problem = False
        if p[0].getUserName() == users[0].getUserName() and p[1].getUserName() == users[5].getUserName() or p[
            0].getUserName() == users[5].getUserName() and p[1].getUserName() == users[0].getUserName() or p[
            0].getUserName() == users[1].getUserName() and p[1].getUserName() == users[6].getUserName() or p[
            0].getUserName() == users[6].getUserName() and p[1].getUserName() == users[1].getUserName():

            print(f"couple detecté: {p[0]} et {p[1]}")
            problem = True
            nbCouple += 1

        if p[0].getUserName() == users[4].getUserName() and p[1].getUserName() == users[6].getUserName() or p[
            0].getUserName() == users[0].getUserName() and p[1].getUserName() == users[1].getUserName() or p[
            0].getUserName() == users[5].getUserName() and p[1].getUserName() == users[4].getUserName() or p[
            0].getUserName() == users[2].getUserName() and p[1].getUserName() == users[8].getUserName():

            print(f"Meme personnes detectées: {p[0]} et {p[1]}")
            problem = True
            nbSame += 1

        # if not problem:
        #     print("OK")

    global_data.Christmas[index].resetPairs()
print(f"couple :{nbCouple}   same: {nbSame}")


# global_data.saveChristmas()
