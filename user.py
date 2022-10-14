import global_data


def getUserByUserName(userName: str):
    if global_data.Users is not None:
        for u in global_data.Users:
            if u.getUserName() == userName:
                return u
    return None


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
    if global_data.Users is None:
        return False
    for u in global_data.Users:
        if u.getUserName() == user.getUserName() or u.getName() == user.getName():
            return True
    return False

