from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from aesa.serializers import PlainSerializer

from .factories import PlainFactory


class PlainSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.plain = PlainFactory.create()

    def test_that_a_plain_is_correctly_serialized(self):
        plain = self.plain
        serializer = PlainSerializer
        serialized_plain = serializer(plain).data

        assert serialized_plain['id'] == plain.id
        assert serialized_plain['name'] == plain.name
        assert serialized_plain['plain_code'] == plain.plain_code
        assert serialized_plain['customer'] == plain.customer
        assert serialized_plain['feeder'] == plain.feeder
        assert serialized_plain['zone'] == plain.zone
        assert serialized_plain['delivery_number'] == plain.delivery_number
        assert serialized_plain['utm_coordinates'] == plain.utm_coordinates
        assert serialized_plain['observation'] == plain.observation
