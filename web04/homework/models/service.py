from mongoengine import *
# create collection, design database
class Service(Document):
    image = URLField()
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    description = StringField()
    measurements = ListField()
