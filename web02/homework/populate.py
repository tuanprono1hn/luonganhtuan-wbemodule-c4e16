from models.customer import Customer
import mlab
from random import randint, choice
from faker import Faker
mlab.connect()
fake = Faker()
for i in range(50):
    print("Saving customer...", i + 1, "...")
    new_customer = Customer(
                            name=fake.name(),
                            gender=randint(0, 1),
                            phone=fake.phone_number(),
                            job=fake.job(),
                            company=fake.company(),
                            contacted=choice([True, False])
                            )
    new_customer.save()
