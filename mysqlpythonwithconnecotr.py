
import mysql.connector

# Establishing connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",  
    password="your_password",
    database="student_records"  
)
cursor = mydb.cursor()

# Creating the students table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_no INT PRIMARY KEY, 
    name VARCHAR(20), 
    grade VARCHAR(20), 
    marks INT
)''')

while True:
    print("\n1. Add Student 2. View Students 3. Exit")
    choice = int(input("Choice: "))
    if choice == 3:
        break
    elif choice == 1:
        roll_no = int(input("Roll No: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
        if cursor.fetchone():
            print("Error: Roll No already exists!")
        else:
            name = input("Name: ")
            grade = input("Grade: ")
            marks = int(input("Marks: "))
            cursor.execute(
                "INSERT INTO students (roll_no, name, grade, marks) VALUES (%s, %s, %s, %s)", 
                (roll_no, name, grade, marks)
            )
            mydb.commit()
            print("Student added successfully.")
    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        for r in cursor.fetchall():
            print("Roll No: " + str(r[0]) + ", Name: " + r[1] + ", Grade: " + r[2] + ", Marks: " + str(r[3]))
    else:
        print("Invalid choice!")

cursor.close()
mydb.close()
