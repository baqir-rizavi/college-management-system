import pymysql
import pymysql.cursors
from InitDB import config


def get_connection():
    return pymysql.connect(
        host=config['host'],
        port=config['port'],
        user=config['user'],
        password=config['password'],
        db=config['database'],
        cursorclass=pymysql.cursors.DictCursor)


class Repository:
    @staticmethod
    def validate_credentials(u, p):
        query = f"""
                    select * from users
                    where username = '{u}'
                    and
                    passwd = '{p}';
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_user_id_by_username(username):
        query = f"""
                    select id from users
                    where username = '{username}';
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchone()['id']
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_teacher_by_usr_id(usr_id):
        query = f"""
                    select * from teacher
                    where usr_id = {usr_id};
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchone()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_student_by_usr_id(usr_id):
        query = f"""
                    select * from student
                    where usr_id = {usr_id};
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchone()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_semester_dues_by_student_id(stu_id):
        query = f"""
                    select semester_dues from student
                    where id = {stu_id};
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchone()['semester_dues']
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def update_semester_dues_by_student_id(id, payment):
        query = f"""
                    update student
                    set semester_dues = {payment}
                    where id = {id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_courses_by_student_id(id):
        query = f"""
                    select c.* from course c, student_enrollment e
                    where c.id = e.cr_id 
                    and
                    e.st_id = {id}
                    order by c.id;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_pending_assignments_by_student_id(id):
        query = f"""
                    select a.* from assignment a, assignment_status at
                    where a.id = at.ass_id
                    and 
                    at.st_id = {id}
                    and 
                    at.is_complete = false;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_courses_by_teacher_id(id):
        query = f"""
                    select * from course
                    where teach_id = {id};
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_students_by_course_id(course_id):
        query = f"""
                    select s.* from student s, student_enrollment e
                    where s.id = e.st_id
                    and 
                    e.cr_id = {course_id}
                    order by s.id;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_attendance_today(stu_id, selected_course_id, is_present):
        query = f"""
                    insert into attendance
                    values ({stu_id}, {selected_course_id}, now(), '{is_present}');
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_assignment(deadline, course_id, title, desc):
        query = f"""
                    insert into assignment (title, description, deadline, cr_id)
                    values ('{title}', '{desc}', '{deadline}', {course_id});
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.lastrowid
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_student(username, password, name, roll_no, batch, semester_dues, current_semester):
        query1 = f"""
                    insert into users (username, passwd, is_admin)
                    values ('{username}', '{password}', false);
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result1 = cur.execute(query1)
            query2 = f"""
                        insert into student (full_name, roll_no, batch, semester_dues, current_semester, usr_id)
                        values ('{name}', '{roll_no}', '{batch}', {semester_dues}, {current_semester}, {cur.lastrowid});
                    """
            result2 = cur.execute(query2)
            if result1 >= 1 and result2 >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def delete_student_by_id(id):
        query = f"""
                    delete from student where id = {id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        # TODO: deleting an invalid id does not print exception (fix the damn thing)
        return ret

    @staticmethod
    def get_all_students():
        query = f"""
                    select * from student;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_enrollment(cr_id, stu_id):
        query = f"""
                    insert into student_enrollment
                    values ({stu_id}, {cr_id}, now());
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_teacher(username, password, name, salary, experience, no_of_courses):
        query1 = f"""
                    insert into users (username, passwd, is_admin)
                    values ('{username}', '{password}', false);
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result1 = cur.execute(query1)
            query2 = f"""
                        insert into teacher (full_name, salary, experience, no_of_courses, usr_id)
                        values ('{name}', {salary}, {experience}, {no_of_courses}, {cur.lastrowid});
                    """
            result2 = cur.execute(query2)
            if result1 >= 1 and result2 >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def assign_teacher_to_course(cr_id, teach_id):
        query1 = f"""
                    update course
                    set teach_id = {teach_id}
                    where id = {cr_id};
                """
        query2 = f"""
                    update teacher
                    set no_of_courses = no_of_courses + 1
                    where id = {teach_id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result1 = cur.execute(query1)
            result2 = cur.execute(query2)
            if result1 >= 1 and result2 >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_course(name, credit_hours):
        query = f"""
                    insert into course (full_name, credit_hours)
                    values ('{name}', {credit_hours});
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def delete_course(id):
        query = f"""
                    delete from course where id = {id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_all_teachers():
        query = f"""
                    select * from teacher;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_all_courses():
        query = f"""
                    select * from course;
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = cur.fetchall()
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def delete_teacher_by_id(id):
        query = f"""
                    delete from teacher where id = {id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def get_is_admin_by_usr_id(id):
        query = f"""
                    select is_admin from users
                    where id = {id};
                """
        ret = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if cur.fetchone()['is_admin']:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def insert_assignment_status(st_id, posted_ass_id, status):
        query = f"""
                    insert into assignment_status
                    values ({st_id}, {posted_ass_id}, {status});
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result = cur.execute(query)
            if result >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret

    @staticmethod
    def update_assignment_status(st_id, ass_id, status):
        query = f"""
                    update assignment_status
                    set is_complete = {status}
                    where st_id = {st_id}
                    and 
                    ass_id = {ass_id};
                """
        ret = False
        try:
            conn = get_connection()
            cur = conn.cursor()
            result1 = cur.execute(query)
            if result1 >= 1:
                ret = True
            conn.commit()
            conn.close()
        except pymysql.Error as e:
            print(e)
        return ret
