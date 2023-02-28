from peewee import *
from os import path




connection = path.dirname(path.relpath(__file__))
db = SqliteDatabase(path.join(connection,"Abiud.db"))


#creating our first table
class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()


    class Meta:
        database = db


Student.create_table(fail_silently=True)