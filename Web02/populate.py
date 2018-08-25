from models.services import Service
from models.customers import Customer
import mlab
from faker import Faker
from random import *

mlab.connect()
fake = Faker()
# for i in range(50):
#     print("Saving customer", i+1, "......")
#     new_customer = Customer(
#         name = fake.name(),
#         gender = randint(0,1),
#         email = fake.email(),
#         phone = fake.phone_number(),
#         job = fake.job(),
#         company = fake.company(),
#         status = choice([True, False])
#     )

#     new_customer.save()

for i in range(50):
    print("Saving service", i+1, "......")
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        height = randint(150,180),
        gender = randint(0,1),
        address = fake.address(),
        phone = fake.phone_number(),
        image = "https://www.google.com.vn/imgres?imgurl=https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/20180602_FIFA_Friendly_Match_Austria_vs._Germany_Joshua_Kimmich_850_0717.jpg/1200px-20180602_FIFA_Friendly_Match_Austria_vs._Germany_Joshua_Kimmich_850_0717.jpg&imgrefurl=https://en.wikipedia.org/wiki/Joshua_Kimmich&h=1800&w=1200&tbnid=6pphxx3pNyygmM:&q=joshua+kimmich&tbnh=186&tbnw=124&usg=AFrqEzeKaH10ftUOSRWsz13rZwUHto1tKw&vet=1&docid=E-SsBYhDOvcMVM&itg=1&sa=X&ved=2ahUKEwj26_mv84XdAhWE7GEKHQXXCUcQ_B0wGXoECAYQCQ",
        description = ["ngoan hiền", "dễ thương", "lễ phép với gia đình"],
        measurements = [90, 60, 90],
        status = choice([True, False])
    )

    new_service.save()