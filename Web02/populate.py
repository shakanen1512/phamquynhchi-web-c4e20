from models.services import Service
from models.customers import Customer
import mlab
from faker import Faker
from random import *

mlab.connect()
fake = Faker()
for i in range(50):
    print("Saving customer", i+1, "......")
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1),
        email = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        status = choice([True, False])
    )

    new_customer.save()