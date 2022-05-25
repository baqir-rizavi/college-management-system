import math
from Repository import Repository as repo
from User import User
import Utils


class Admin(User):

    def login(self):
        User.login(self)
        if repo.get_is_admin_by_usr_id(User.get_usr_id(self)) is None:
            print("user not an admin!!!!")
            return None
        return True

    def control_flow(self):
        sub_menus_control_flow = [self.student_menu_control_flow, self.teacher_menu_control_flow,
                                  self.course_menu_control_flow]
        option = Admin.menu()
        while option != 4:
            sub_menus_control_flow[option - 1]()
            option = Admin.menu()

    def student_menu_control_flow(self):
        features = [self.add_student, self.update_student, self.delete_student, self.view_all_student,
                    self.display_semester_dues, self.course_to_student]
        option = Admin.student_menu()
        while option != 7:
            features[option - 1]()
            option = Admin.student_menu()

    def teacher_menu_control_flow(self):
        features = [self.add_teacher, self.update_teacher, self.delete_teacher, self.view_all_teacher,
                    self.course_to_teacher]
        option = Admin.teacher_menu()
        while option != 6:
            features[option - 1]()
            option = Admin.teacher_menu()

    def course_menu_control_flow(self):
        features = [self.add_course, self.update_course, self.delete_course, self.view_all_course]
        option = Admin.course_menu()
        while option != 5:
            features[option - 1]()
            option = Admin.course_menu()

    @staticmethod
    def menu():
        print("""--------------------- Admin --------------------------
        ● Enter 1 to Manage Students
        ● Enter 2 to Manage Teachers
        ● Enter 3 to Manage Courses
        ● Enter 4 to logout 
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 4)

    @staticmethod
    def student_menu():
        print("""--------------------- Admin: student management --------------------------
        ● Enter 1 to Add Student
        ● Enter 2 to Update Student
        ● Enter 3 to Delete Student
        ● Enter 4 to View All Students
        ● Enter 5 to Display Outstanding Semester Dues
        ● Enter 6 to Assign Course to Student
        ● Enter 7 to back
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 7)

    @staticmethod
    def teacher_menu():
        print("""--------------------- Admin: teacher management --------------------------
        ● Enter 1 to Add Teacher
        ● Enter 2 to Update Teacher
        ● Enter 3 to Delete Teacher
        ● Enter 4 to View All Teachers
        ● Enter 5 to Assign Course to Teacher
        ● Enter 6 to back
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 6)

    @staticmethod
    def course_menu():
        print("""--------------------- Admin: course management --------------------------
        ● Enter 1 to Add Courses
        ● Enter 2 to Update Courses
        ● Enter 3 to Delete Courses
        ● Enter 4 to View All Courses
        ● Enter 5 to back
        """)
        return Utils.input_validated_int_range("enter option: ", 1, 6)

    @staticmethod
    def add_student():
        print('---adding a student---')
        username = input('enter a username: ')
        password = input('enter a password: ')
        name = input('enter student name: ')
        roll_no = input('enter roll no: ')
        batch = input('enter batch: ')
        semester_dues = Utils.input_validated_int_range('enter semester dues: ', 0, math.inf)
        current_semester = Utils.input_validated_int('enter current semester: ')

        repo.insert_student(username, password, name, roll_no, batch, semester_dues, current_semester)

    @staticmethod
    def delete_student():
        id = input('enter student id to delete: ')
        repo.delete_student_by_id(id)

    @staticmethod
    def update_student():
        dictionary = {}
        id = Utils.input_validated_int('enter student "id" to update: ')
        username = input('enter a username: ')
        if username != '':
            dictionary['username'] = username
        password = input('enter a password: ')
        if password != '':
            dictionary['passwd'] = password
        dictionary2 = {}
        name = input('enter student name: ')
        if name != '':
            dictionary2['full_name'] = name
        roll_no = input('enter roll no: ')
        if roll_no != '':
            dictionary2['roll_no'] = roll_no
        batch = input('enter batch: ')
        if batch != '':
            dictionary2['batch'] = batch
        try:
            semester_dues = input('enter semester dues: ')
            if semester_dues != '':
                semester_dues = int(semester_dues)
                dictionary2['semester_dues'] = semester_dues
            current_semester = input('enter current semester: ')
            if current_semester != '':
                current_semester = int(current_semester)
                dictionary2['current_semester'] = current_semester
        except ValueError as e:
            print(e, ' try updating again')
            return
        if len(dictionary) != 0:
            repo.update_users_by_usr_id(repo.get_usr_id_by_student_id(id), dictionary)
        if len(dictionary2) != 0:
            repo.update_student_by_id(id, dictionary2)

    @staticmethod
    def view_all_student():
        stu = repo.get_all_students()
        if stu is not None:
            for student in stu:
                for item in student.items():
                    print(item)
                print('--------------------')

    @staticmethod
    def display_semester_dues():
        id = Utils.input_validated_int('enter "id" of student for semester dues: ')
        print("dues: ", repo.get_semester_dues_by_student_id(id))

    @staticmethod
    def course_to_student():
        cr_id = Utils.input_validated_int('enter "id" of course: ')
        stu_id = Utils.input_validated_int('enter "id" of student: ')
        repo.insert_enrollment(cr_id, stu_id)

    @staticmethod
    def add_teacher():
        print('---adding a teacher---')
        username = input('enter a username: ')
        password = input('enter a password: ')
        name = input('enter name: ')
        salary = Utils.input_validated_int('enter salary: ')
        experience = Utils.input_validated_float('enter experience in years(float): ')
        no_of_courses = 0
        repo.insert_teacher(username, password, name, salary, experience, no_of_courses)

    @staticmethod
    def update_teacher():
        dictionary = {}
        id = Utils.input_validated_int('enter teacher "id" to update: ')
        username = input('enter a username: ')
        if username != '':
            dictionary['username'] = username
        password = input('enter a password: ')
        if password != '':
            dictionary['passwd'] = password
        dictionary2 = {}
        name = input('enter name: ')
        if name != '':
            dictionary2['full_name'] = name
        try:
            salary = input('enter salary: ')
            if salary != '':
                dictionary2['salary'] = int(salary)
            experience = input('enter experience (float): ')
            if experience != '':
                dictionary2['experience'] = float(experience)
        except ValueError as e:
            print(e, ' try updating again')
            return
        if len(dictionary) != 0:
            repo.update_users_by_usr_id(repo.get_usr_id_by_teacher_id(id), dictionary)
        if len(dictionary2) == 0:
            repo.update_teacher_by_id(id, dictionary2)

    @staticmethod
    def delete_teacher():
        id = input('enter  teacher id to delete: ')
        for courses in repo.get_courses_by_teacher_id(id):
            repo.update_course_teach_id_by_id(courses['id'])
        repo.delete_teacher_by_id(id)

    @staticmethod
    def view_all_teacher():
        teach = repo.get_all_teachers()
        if teach is not None:
            for t in teach:
                for item in t.items():
                    print(item)
                print('--------------------')

    @staticmethod
    def course_to_teacher():
        cr_id = Utils.input_validated_int('enter "id" of course: ')
        teach_id = Utils.input_validated_int('enter "id" of teacher: ')
        repo.assign_teacher_to_course(cr_id, teach_id)

    @staticmethod
    def add_course():
        name = input("enter course name: ")
        credit_hours = Utils.input_validated_int_range("enter credit hour for the course: ", 1, math.inf)
        repo.insert_course(name, credit_hours)

    @classmethod
    def update_course(cls):
        pass  # TODO: complete

    @classmethod
    def delete_course(cls):
        id = Utils.input_validated_int_range("enter id for course you want to delete: ", 0, math.inf)
        repo.delete_course(id)
        print('done')

    @classmethod
    def view_all_course(cls):
        cr = repo.get_all_courses()
        if cr is not None:
            for c in cr:
                for item in c.items():
                    print(item)
                print('--------------------')
