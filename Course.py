
class Course:
    __id: int
    __name: str
    __credit_hours: int

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credit_hours(self):
        return self.__credit_hours

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_credit_hours(self, credit_hours):
        self.__credit_hours = credit_hours
