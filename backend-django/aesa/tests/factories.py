from random import randint, uniform

import factory
from factory import LazyAttribute, LazyFunction, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from faker import Factory

from aesa.models import Plain, Project

faker = Factory.create()


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    ruc = LazyAttribute(lambda o: faker.text(max_nb_chars=20))
    social_reason = LazyAttribute(lambda o: faker.text(max_nb_chars=255))


class PlainFactory(DjangoModelFactory):
    class Meta:
        model = Plain

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    plain_code = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    customer = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    feeder = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    zone = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    delivery_number = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    utm_coordinates = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    observation = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
