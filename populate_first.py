from os import environ

environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django

django.setup()

import random
from first_app.models import AccessRecords, Topic, WebPage
from faker import Faker

fake_generator = Faker()
topics = ["Search", "Marketplace", "Social", "News", "Games"]


def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(populateNumbers=5):
    for number in range(populateNumbers):
        # generate a fake topic
        randomTopic = add_topics()
        # create the fake data for the fake topic
        fakeUrl = fake_generator.url()
        fakeDate = fake_generator.date()
        fakeName = fake_generator.company()

        # create fake web data to the webpage
        fakeWeb = WebPage.objects.get_or_create(
            topic=randomTopic, url=fakeUrl, name=fakeName
        )[0]

        # create a fake access records
        fakeAcc = AccessRecords.objects.get_or_create(name=fakeWeb, date=fakeDate)[0]


if __name__ == "__main__":
    print("populating script!")
    populateNum = input("input a number")
    populate(int(populateNum))
    print("populating complete")
