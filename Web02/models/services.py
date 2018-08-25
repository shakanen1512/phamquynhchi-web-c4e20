from mongoengine import *

#design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    image = StringField()
    description = ListField()
    measurements = ListField()
    status = BooleanField()