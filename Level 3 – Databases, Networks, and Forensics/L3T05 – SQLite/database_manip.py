# Auto-Grade Task L3T05:

import sqlite3

# Connect to database
conn = sqlite3.connect("python_programming.db")
cursor = conn.cursor()

# Creating table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id    INTEGER PRIMARY KEY,
        name  TEXT    NOT NULL,
        grade INTEGER NOT NULL
    )
''')
conn.commit()
print("Table 'Python_Programming' has been successfully created.\n")

# Inserting rows
students = [
    (55, 'Carl Davis',         61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards',      78),
    (12, 'Peyton Sawyer',      45),
    (2,  'Lucas Brooke',       99),
]

cursor.executemany(
    'INSERT OR IGNORE INTO python_programming (id, name, grade) VALUES (?, ?, ?)',
    students
)
conn.commit()
print("Rows inserted successfully.\n")

# Select records with grade between 60 and 80
print("Students with a grade between 60 and 80:")
cursor.execute(
    'SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80'
)
for row in cursor.fetchall():
    print(f"  id={row[0]}, name={row[1]}, grade={row[2]}")

# Update Carl Davis's grade to 65
cursor.execute(
    "UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'"
)
conn.commit()
print("\nCarl Davis's grade updated to 65.")

# Delete Dennis Fredrickson's row
cursor.execute(
    "DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'"
)
conn.commit()
print("Dennis Fredrickson's row deleted.")

# Change grade to 80 for all students with id > 55
cursor.execute(
    'UPDATE python_programming SET grade = 80 WHERE id > 55'
)
conn.commit()
print("Grade updated to 80 for all students with id > 55.\n")

# Final table
print("Final table contents:")
cursor.execute('SELECT * FROM python_programming')
for row in cursor.fetchall():
    print(f"  id={row[0]}, name={row[1]}, grade={row[2]}")

conn.close()
