from peewee import *
from os import path


connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Victor.db"))

#creating our first table


class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently=True)





from peewee import *
from os import path


connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Victor.db"))

#creating our first table


class Teacher(Model):
    Teacher_name = CharField()
    Teacher_email = CharField()
    Teacher_password = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently=True)



from peewee import *
from os import path


connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Victor.db"))

#creating our first table


class Product(Model):
    Product_price = CharField()
    Product_quantity = CharField()
    Product_description = CharField()
    product_color = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently=True)


from peewee import *
from os import path


connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Victor.db"))

#creating our first table


class User(Model):
    User_name = CharField()
    User_phone = CharField()
    User_email = CharField()
    User_password = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently=True)
