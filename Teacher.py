from Repository import Repository as repo
from User import User
import Utils


class Teacher(User):
    __id: int
    __name: str
    __salary: int
    __experience: float
    __no_of_courses: int

    def login(self):
        User.login(self)
        teacher = repo.get_teacher_by_usr_id(User.get_usr_id(self))
        if teacher is None:
            print("login failed: plz login as 'teacher'!!!")
            return None
        self.__id = teacher['id']
        self.__name = teacher['full_name']
        self.__salary = teacher['salary']
        self.__experience = teacher['experience']
        self.__no_of_courses = teacher['no_of_courses']
        return teacher

    @staticmethod
    def menu():
        print("""---------------------- Teacher --------------------------
        ● Enter 1 to Mark attendance
        ● Enter 2 to post assignment
        ● Enter 3 to View Assigned Courses
        ● Enter 4 to logout
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 4)

    def control_flow(self):
        features = [self.mark_attendance, self.post_assignment, self.view_assigned_courses]
        option = Teacher.menu()
        while option != 4:
            features[option - 1]()
            option = Teacher.menu()

    def mark_attendance(self):
        assigned_courses = repo.get_courses_by_teacher_id(self.__id)
        if assigned_courses is not None:
            assigned_courses_ids = [assigned_course['id'] for assigned_course in assigned_courses]
            for c in assigned_courses:
                for item in c.items():
                    print(item)
                print('--------------------')
            selected_course_id = Utils.input_validated_int_in('enter course "id" to mark attendance of: ',
                                                              assigned_courses_ids, 'id entered not found')

            students = repo.get_students_by_course_id(selected_course_id)
            print('student id\tstudent name\tattendance')
            for student in students:
                print(student['id'], '\t', student['full_name'] + '\t', end='')
                is_present = Utils.input_validated_in("('a' or 'p'): ", ['a', 'p'])
                repo.insert_attendance_today(student['id'], selected_course_id, is_present)
        else:
            print('no course yet')

    def post_assignment(self):
        assigned_courses = repo.get_courses_by_teacher_id(self.__id)
        if assigned_courses is None:
            print("no course to post assignment on")
            return

        assigned_courses_ids = [assigned_course['id'] for assigned_course in assigned_courses]
        for c in assigned_courses:
            for item in c.items():
                print(item)
            print('--------------------')
        selected_course_id = Utils.input_validated_int_in('enter course "id" to post assignment: ',
                                                          assigned_courses_ids, 'id entered not found')
        print('.set the deadline.')
        deadline = Utils.input_validated_date()
        title = input('enter title: ')
        desc = input('enter description: ')
        posted_ass_id = repo.insert_assignment(deadline, selected_course_id, title, desc)

        # every student will get an uncompleted assignment record

        students = repo.get_students_by_course_id(selected_course_id)
        if students is not None:
            for student in students:
                repo.insert_assignment_status(student['id'], posted_ass_id, False)

    def view_assigned_courses(self):
        assigned_courses = repo.get_courses_by_teacher_id(self.__id)
        if assigned_courses is not None:
            print('id\tname')
            for course in assigned_courses:
                print(course['id'], '\t', course['full_name'])
        else:
            print('no assigned courses')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_experience(self):
        return self.__experience

    def get_no_of_courses(self):
        return self.__no_of_courses

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_experience(self, experience):
        self.__experience = experience

    def set_no_of_courses(self, no_of_courses):
        self.__no_of_courses = no_of_courses
