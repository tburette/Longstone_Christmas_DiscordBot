import global_data

class User:
    def __init__(self, user_name: str, name: str):
        self.user_name = user_name
        self.name = name

    def getUserName(self):
        return self.user_name

    def getName(self):
        return self.name

    def toString(self):
        return f"{self.getUserName()} - {self.getName()}"


def exist(user: User) -> bool:
    for u in global_data.Users:
        if u.getUserName() == user.getUserName() or u.getName() == user.getName():
            return True
    return False

