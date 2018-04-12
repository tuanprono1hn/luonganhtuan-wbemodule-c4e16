from mongoengine import *
import datetime
class Order(Document):
    userid = StringField()
    serviceid = StringField()
    time = DateTimeField(default=datetime.datetime.now)
    is_accepted = BooleanField()
