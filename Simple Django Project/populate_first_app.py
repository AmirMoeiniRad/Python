import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_first_project.settings')

import django
django.setup()

# Fake population script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fake_gen = Faker()
topics = ['Search','Social','MarketPlace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):

        # Get the topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # create new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake access record fot that entry
        acc_rec = AccessRecord.objects.get_or_create(topic=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('Populating...')
    populate(n=20)
    print('Done.')
