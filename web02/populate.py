from models.service import Service
import mlab
from random import randint, choice
from faker import Faker
mlab.connect()
fake = Faker()
img_list = ["https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg"]
for i in range(20):
    print("Saving service", i + 1, "...")
    new_service = Service(
                            image=img_list[i],
                            name=fake.name_female(),
                            yob=randint(1995,2000),
                            gender=choice([0,1]),
                            height=randint(150,170),
                            phone=fake.phone_number(),
                            description=fake.sentence(nb_words=15, variable_nb_words=True, ext_word_list=None),
                            measurements=[randint(80,100), randint(55,70), randint(85,110)]
                            )
    new_service.save()
# print(fake.address())
