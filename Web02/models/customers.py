from mongoengine import *

#design database
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    status = BooleanField()