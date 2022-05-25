from Repository import Repository as repo
from User import User
import Utils


class Student(User):
    __id: int
    __name: str
    __roll_no: str
    __batch: str
    __semester_dues: int
    __current_semester: int

    def login(self):
        User.login(self)
        student = repo.get_student_by_usr_id(User.get_usr_id(self))
        if student is None:
            print("login failed: plz login as 'student'!!!")
            return None
        self.__id = student['id']
        self.__name = student['full_name']
        self.__roll_no = student['roll_no']
        self.__batch = student['batch']
        self.__semester_dues = student['semester_dues']
        self.__current_semester = student['current_semester']
        return student

    @staticmethod
    def menu():
        print("""----------------------- Student --------------------------
        ● Enter 1 to Pay Semester Dues
        ● Enter 2 to view enrolled courses
        ● Enter 3 to view pending Assignments
        ● Enter 4 to mark assignment as complete
        ● Enter 5 to logout
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 5)

    def control_flow(self):
        features = [self.pay_semester_dues, self.view_enrolled_courses, self.view_pending_assignments,
                    self.mark_assignment_complete]
        option = Student.menu()
        while option != 5:
            features[option - 1]()
            option = Student.menu()

    def pay_semester_dues(self):
        remaining_dues = repo.get_semester_dues_by_student_id(self.__id)
        if remaining_dues != 0:
            payment = Utils.input_validated_int_range("enter the amount you want to pay: ", 1, remaining_dues,
                                                      additional_error_info="amount is more than the dues")
            repo.update_semester_dues_by_student_id(self.__id, remaining_dues - payment)
            print("new remaining dues are ", remaining_dues - payment)
        else:
            print("all dues paid!")

    def view_enrolled_courses(self):
        courses_array = repo.get_courses_by_student_id(self.__id)
        if courses_array is not None:
            print('id\tcourse')
            for course in courses_array:
                print(course['id'], '\t', course['full_name'])
        else:
            print('no course added')

    def view_pending_assignments(self):
        pending_assignments = repo.get_pending_assignments_by_student_id(self.__id)
        if pending_assignments is not None:
            print('Assignment\tdeadline')
            for pending_assignment in pending_assignments:
                print(pending_assignment['title'], '\t', pending_assignment['deadline'])
        else:
            print("no assignments yet")

    def mark_assignment_complete(self):
        pending_assignments = repo.get_pending_assignments_by_student_id(self.__id)
        print("following are pending assignments, to marks as complete press '1' otherwise '0' if still pending")
        if pending_assignments is not None:
            print('id\tAssignment')
            for pending_assignment in pending_assignments:
                print(pending_assignment['id'], '\t', pending_assignment['title'], end='\t')
                if Utils.input_validated_int_range("('0' or '1'): ", 0, 1):
                    repo.update_assignment_status(self.__id, pending_assignment['id'], True)
        else:
            print("no assignments yet")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_batch(self):
        return self.__batch

    def get_semester_dues(self):
        return self.__semester_dues

    def get_current_semester(self):
        return self.__current_semester

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def set_batch(self, batch):
        self.__batch = batch

    def set_semester_dues(self, semester_dues):
        self.__semester_dues = semester_dues

    def set_current_semester(self, current_semester):
        self.__current_semester = current_semester
