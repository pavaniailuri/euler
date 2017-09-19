import peewee
from peewee import *

db = MySQLDatabase('databasename', user='username', passwd='password')

class Book(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db

Empdetails.create_table()
emp = Empdetails(empname="name", designation='Emp designation')
emp.save()
for emp in Empdetails.filter(empname="name of the emp"):
    print emp.designation
