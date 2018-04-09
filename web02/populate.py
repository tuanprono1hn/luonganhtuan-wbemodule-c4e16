from models.service import Service
import mlab
from random import randint, choice
from faker import Faker
mlab.connect()
fake = Faker()
img_list = ["https://image.freepik.com/free-photo/hair-style-street-fashion-beautiful-girl_1139-844.jpg",
            "https://drive.google.com/open?id=1w6MEZYNJjsWRyylyJrEPjxJomU5lO4JO",
            "https://drive.google.com/open?id=1e6P2ljCQlFX6RPrNClwTUsiheUCTnHl-",
            "https://drive.google.com/open?id=1zlOKHqoZhiJ4uq2IXRszDvwU1gT_ZeOa",
            "https://drive.google.com/open?id=15ru3XahCkLE0Yt5yR1K-fAJ8wcF8dXPi",
            "https://drive.google.com/open?id=1qRPXSjOvVvRvH0VH64Yl4h09zke6HxEU",
            "https://drive.google.com/open?id=12HgUSIursvDX8UMDVJskM-bGADKO-Pfa",
            "https://drive.google.com/open?id=1DtxfGcUd4FVvWY375XFxKh-7N_9QlBGd",
            "https://drive.google.com/open?id=1UeSZp7KWOpeOUZVSmeaZuAe0rt81EeT2",
            "https://drive.google.com/open?id=1ANvmXA3DbsDZsmniYpsqXVNy8z3YwaAG",
            "https://drive.google.com/open?id=127_PtDGZbGksUb6z2ppAJbeP3Z2NUKYR",
            "https://drive.google.com/open?id=1ROGZ107jkWXpnpdfrbwAg3a0rreeOTnP",
            "https://drive.google.com/open?id=1TihEuBzLPe2t5yWXAWH0tYXOkBA306rF",
            "https://drive.google.com/open?id=1SwAMxhWpo2ZZsifA-8YHHBWtApYp17nS",
            "https://drive.google.com/open?id=1DLWKOvGlUEjW3xBBgUSEa-xapn8shJVB",
            "https://drive.google.com/open?id=15IQ4-CS7UHYdFkTycxsV4tWT31y2OE0X",
            "https://drive.google.com/open?id=1EnealIklkSea0U-DXs91gglXLOQCqBH1",
            "https://drive.google.com/open?id=1xmAa6SzTYk5_sTbBKl7e8kPqBs6jGyAy",
            "https://drive.google.com/open?id=17WahNbv2smjVg7zLfJ7YkxnHV67J_DIB",
            "https://drive.google.com/open?id=1y2FAPNJ25jdaZJdJp2u02PBeZcl4zdzR"]
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
