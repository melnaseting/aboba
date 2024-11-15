import sqlite3

conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE if NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age Int,
                major TEXT)
                """)
cursor.execute("""CREATE TABLE if NOT EXISTS courses (
                    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT,
                    instructor TEXT)
               """)
cursor.execute("""CREATE TABLE IF NOT EXISTS student_courses (
                    student_id INTEGER,
                    course_id INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (course_id) REFERENCES courses(course_id),
                    PRIMARY KEY (student_id, course_id))
               """)

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        try:
            name_input = str(input("name:"))
            age_input = int(input("age:"))
            major_input = str(input("major:"))
        except:
            print("TypeError: 'NoneType'")
        cursor.execute(f"INSERT INTO students(name,age,major) VALUES ('{name_input}',{age_input},'{major_input}')")
        conn.commit()
        # Додавання нового студента

    elif choice == "2":
        try:
            course_name_input = str(input("course_name:"))
            instructor_input = str(input("instructor:"))
            

        except:
            print("TypeError: 'NoneType'")
        cursor.execute(f"INSERT INTO courses(course_name,instructor) VALUES ('{course_name_input}','{instructor_input}')")
        conn.commit()
        # Додавання нового курсу

    elif choice == "3":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
 
        if not students:
            print("У базі даних немає зареєстрованих студентів.")
        else:
            print("\nСписок студентів:")
            for student in students:
                print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")

     
    elif choice == "4":
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
 
        if not courses:
            print("У базі даних немає зареєстрованих студентів.")
        else:
            print("\nСписок студентів:")
            for course in courses:
                print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")
        # Показати список курсів

    elif choice == "5":
        student_id = int(input("Введіть ID студента: "))
        course_id = int(input("Введіть ID курсу: "))
 
        # Зареєструвати студента на курс
        cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
 
    elif choice == "6":
        # Показати студентів на конкретному курсі
        course_id = int(input("Введіть ID курсу для фільтрації: "))
        cursor.execute('''SELECT students.id, students.name, students.age, students.major
                          FROM students, student_courses
                          WHERE students.id = student_courses.student_id
                          AND student_courses.course_id = ?''', (course_id,))
        students_on_course = cursor.fetchall()
 
        if not students_on_course:
            print(f"На курсі з ID {course_id} немає зареєстрованих студентів.")
        else:
            print(f"\nСписок студентів на курсі з ID {course_id}:")
            for student in students_on_course:
                print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")

       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")