from main import Teacher

teachers = Teacher.select()
for teacher in teachers:
    print(teacher.teach_name, teacher.teach_email, teacher.teach_password)
