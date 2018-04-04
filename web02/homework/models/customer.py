from mongoengine import *
class Customer(Document):
    name = StringField()
    gender = IntField() #0: Female 1: Male
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted=BooleanField()
