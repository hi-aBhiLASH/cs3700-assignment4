#!/usr/bin/env python 3

import sys
import mysql.connector
from mysql.connector import Error



def get_connection():
    
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "academic_insti"
    )



FAIL_GRADES = ('U', 'E')
SEM  = 'Even'
YEAR = 2006


def print_header(title: str):
    print("\n" + "═" * 55)
    print(f"  {title}")
    print("═" * 55)
 
 
def print_success(msg: str):
    print(f"\n  ✔  {msg}")
 
 
def print_error(msg: str):
    print(f"\n  ✘  {msg}")
 
 
def print_info(msg: str):
    print(f"     {msg}")




def add_course(conn):
    print_header("FEATURE 1 — Add Course  (Even Semester 2006)")
 
    dept_id    = input("\n  Enter Department ID   : ").strip()
    course_id  = input("  Enter Course ID       : ").strip()
    teacher_id = input("  Enter Teacher (Emp) ID: ").strip()
    classroom  = input("  Enter Classroom       : ").strip()
 
    cursor = conn.cursor(dictionary=True)


    # validate dept exists
    cursor.execute("SELECT deptId, name FROM department WHERE deptId = %s", (dept_id,))
    dept = cursor.fetchone()
    if not dept:
        print_error(f"Department '{dept_id}' does not exist.")
        cursor.close()
        return
    print_info(f"Department found: {dept['name']}")



    # validate course exists and belongs to this dept
    cursor.execute(
        "SELECT courseId, cname, deptNo FROM course WHERE courseId = %s",
        (course_id,)
    )
    course = cursor.fetchone()
    if not course:
        print_error(f"Course '{course_id}' does not exist in the database.")
        cursor.close()
        return
    if course['deptNo'] != dept_id:
        print_error(
            f"Course '{course_id}' ({course['cname']}) belongs to "
            f"dept '{course['deptNo']}', not dept '{dept_id}'."
        )
        cursor.close()
        return
    print_info(f"Course found: {course['cname']}")



    # validate teacher exists and belongs to this dept
    cursor.execute(
        "SELECT empId, name, deptNo FROM professor WHERE empId = %s",
        (teacher_id,)
    )
    teacher = cursor.fetchone()
    if not teacher:
        print_error(f"Professor with empId '{teacher_id}' does not exist.")
        cursor.close()
        return
    if teacher['deptNo'] != dept_id:
        print_error(
            f"Professor '{teacher_id}' ({teacher['name']}) belongs to "
            f"dept '{teacher['deptNo']}', not dept '{dept_id}'."
        )
        cursor.close()
        return
    print_info(f"Professor found: {teacher['name']}")


    # check for duplicate teaching entry in the same year/sem
    cursor.execute(
        """SELECT 1 FROM teaching
           WHERE empId=%s AND courseId=%s AND sem=%s AND year=%s""",
        (teacher_id, course_id, SEM, YEAR)
    )
    if cursor.fetchone():
        print_error(
            f"Professor '{teacher_id}' is already assigned to course "
            f"'{course_id}' in Even 2006."
        )
        cursor.close()
        return
 


    # insert data into teaching
    cursor.execute(
        """INSERT INTO teaching (empId, courseId, sem, year, classRoom)
           VALUES (%s, %s, %s, %s, %s)""",
        (teacher_id, course_id, SEM, YEAR, classroom)
    )
    conn.commit()
 
    print_success(
        f"Course '{course_id}' ({course['cname']}) successfully added!\n"
        f"     Taught by : {teacher['name']}  |  Room: {classroom}  |  {SEM} {YEAR}"
    )
    cursor.close()


def enroll_student(conn):
    pass




def main():
    print("\n" + "═" * 55)
    print("   Academic Institution DB — Assignment 4A")
    print("═" * 55)


    try:
        conn = get_connection()
        print_info("Connected to database 'academic_insti'.")
    except Error as e:
        print_error(f"Could not connect to database: {e}")
        sys.exit(1)


    while True:

        print("\n  MAIN MENU")
        print("  ─────────────────────────────────────")
        print("  1. Add course (Even Semester 2006)")
        print("  2. Enroll student (Even Semester 2006)")
        print("  3. Exit")
        print("  ─────────────────────────────────────")
        choice = input("  Enter choice [1/2/3]: ").strip()

        if choice == "1":
            try:
                add_course(conn)
            except Error as e:
                print_error(f"Database error: {e}")

        elif choice == "2":
            try:
                enroll_student(conn)
            except Error as e:
                print_error(f"Database error: {e}")


        elif choice == "3":
            print("\n  Closing!\n")
            break
 
        else:
            print_error("Invalid choice. Enter 1, 2, or 3.")
    
    conn.close()


if __name__ == "__main__":
    main()