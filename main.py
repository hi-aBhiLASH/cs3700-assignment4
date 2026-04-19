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