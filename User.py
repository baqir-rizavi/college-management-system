from Repository import Repository as repo


class User:
    __usr_id: int
    __username: str
    __password: str

    def login(self):
        u, p = input("enter username: "), input("enter password: ")
        while not repo.validate_credentials(u, p):
            print("incorrect username or password! enter again")
            u, p = input("enter username: "), input("enter password: ")
        self.__username = u
        self.__password = p
        self.__usr_id = repo.get_user_id_by_username(self.__username)

    @staticmethod
    def menu():
        pass

    def control_flow(self):
        pass

    def get_usr_id(self):
        return self.__usr_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_usr_id(self, usr_id):
        self.__usr_id = usr_id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password
