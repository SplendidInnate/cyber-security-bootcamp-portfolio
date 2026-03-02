""""This module provides a function to connect to a SQLite database,"""
import sqlite3


def get_sql_cursor():
    """
    Establishes a connection to "StudentDatabase.db", sets up the database
    schema by dropping any existing "Student" table, creating a new one,
    and inserting initial data. Returns a cursor for further database
    operations.

    Returns:
        sqlite3.Cursor: Cursor for database interaction.
    """
    conn = sqlite3.connect("StudentDatabase.db")
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Student;')

    with open("SQLFiles/create_student_table.sql",
              encoding='utf-8') as create_stu_file:
        cursor.execute(create_stu_file.read())

    with open("SQLFiles/insert_student_values.sql",
              encoding='utf-8') as insert_stu_file:
        cursor.execute(insert_stu_file.read())
    return cursor

