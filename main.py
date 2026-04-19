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
    pass


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