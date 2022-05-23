import Utils
from Admin import Admin
from Student import Student
from Teacher import Teacher
from User import User


class Portal(object):

    __current_user: User

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def menu():
        print("======================= WELCOME TO CMS =======================")
        print("""
                ● Enter 1 to login as Admin
                ● Enter 2 to login as Student
                ● Enter 3 to login as Teacher
                ● Enter 4 to Exit
                """)
        return Utils.input_validated_int_range("enter option: ", 1, 4)

    def run(self):
        option = Portal.menu()
        while option != 4:
            if option == 1:
                self.__current_user = Admin()
            if option == 2:
                self.__current_user = Student()
            if option == 3:
                self.__current_user = Teacher()

            log = self.__current_user.login()   # polymorphism achieved
            if log is not None:
                self.__current_user.control_flow()
            option = Portal.menu()
