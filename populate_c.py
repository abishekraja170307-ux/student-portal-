import sqlite3


def display_students(cursor, title):
    cursor.execute("SELECT id, name, age, course FROM students")
    students = cursor.fetchall()

    print(f"\n{title}")
    print("ID | Name | Age | Course")
    print("---|------|-----|-------")
    for student_id, name, age, course in students:
        print(f"{student_id} | {name} | {age} | {course}")


connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# CREATE: insert a new record
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Ragul", 21, "Python")
)
student_id = cursor.lastrowid
connection.commit()
display_students(cursor, "After CREATE")

# UPDATE: change the new record
cursor.execute(
    "UPDATE students SET name = ?, course = ? WHERE id = ?",
    ("Ragul Kumar", "SQL", student_id)
)
connection.commit()
display_students(cursor, "After UPDATE")

# DELETE: remove only the demo record
cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
connection.commit()
display_students(cursor, "After DELETE")

connection.close()
print("\nCRUD process completed successfully")