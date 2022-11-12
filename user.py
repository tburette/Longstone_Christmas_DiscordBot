import global_data


def getUserByUserName(userName: str):
    if global_data.Users is not None:
        for u in global_data.Users:
            if u.getUserName() == userName:
                return u
    return None

def getIndexUserByUserName(userName: str):
    i = 0
    if global_data.Users is not None:
        for u in global_data.Users:
            if u.getUserName() == userName:
                return i
            i += 1
    return -1


def getUserByName(Name: str):
    if global_data.Users is not None:
        for u in global_data.Users:
            if u.getName() == Name:
                return u
    return None


class User:
    def __init__(self, user_name: str, name: str):
        self.user_name = user_name
        self.name = name
        self.partner = None

    def getUserName(self):
        return self.user_name

    def getName(self):
        return self.name

    def setPartner(self, partner_name: str):
        partner = None

        if self.getPartner() is not None:
            message = f"{self.getName()}, \nTu es déjà en couple avec {self.getPartner().getName()}"
            return message

        for p in global_data.Users:
            if p.getName().lower() == partner_name.lower():
                partner = p
                break
        if partner is None:
            message = f"Aouch... de pire en pire, ton conjoint n'existe pas... soit il n'est pas inscrit, soit il " \
                      f"a pas dis la vérité sur son nom, soit il existe dans ta tête.\n" \
                      f"Mon hypotèse est qu'il n'a pas dit son vrai nom..." \
                      f" Tu peux le découvrir en tapant la commande $qui_est_qui.\n"
            return message
        else:
            if partner.getPartner() is not None:
                message = f"Aouch... désolé, ton conjoint n'est pas fidèle... Il est déjà en couple avec" \
                          f" {partner.getPartner().getName()}.\nJe vous laisse vous débrouiller"
                return message
            else:
                self.partner = partner

                global_data.Users[getIndexUserByUserName(partner.getUserName())].partner = self
                message = f"C'est beau l'amour!!! Plein de bonheur à {self.getName()} et {partner.getName()}"
                return message

    def removePartner(self):
        partner = ""
        if self.getPartner() != None:
            partner = self.getPartner().getName()
            self.partner.partner = None
            self.partner = None
            return f"{self.getName()} n'est plus en couple avec {partner}"
        return f"{self.getName()} c'est triste mais tu n'est pas en couple"


    def getPartner(self):
        return self.partner

    def toString(self):
        return f"{self.getUserName()} - {self.getName()}"

    async def sendPrivateMessage(self, ctx, message):
        members = ctx.channel.members
        member = None
        for m in members:
            if str(m) == self.getUserName():
                member = m
                break
        await member.send(message)

    def __str__(self):
        return self.getUserName() + " - " + self.getName()


def exist(user: User) -> bool:
    if global_data.Users is None:
        return False
    for u in global_data.Users:
        if u.getUserName() == user.getUserName() or u.getName() == user.getName():
            return True
    return False




