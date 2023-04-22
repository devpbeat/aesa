import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Plain
from .factories import PlainFactory, ProjectFactory

faker = Factory.create()


class Plain_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        PlainFactory.create_batch(size=3)

    def test_create_plain(self):
        """
        Ensure we can create a new plain object.
        """
        client = self.api_client
        plain_count = Plain.objects.count()
        plain_dict = factory.build(dict, FACTORY_CLASS=PlainFactory)
        response = client.post(reverse('plain-list'), plain_dict)
        created_plain_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert Plain.objects.count() == plain_count + 1
        plain = Plain.objects.get(pk=created_plain_pk)

        assert plain_dict['name'] == plain.name
        assert plain_dict['plain_code'] == plain.plain_code
        assert plain_dict['customer'] == plain.customer
        assert plain_dict['feeder'] == plain.feeder
        assert plain_dict['zone'] == plain.zone
        assert plain_dict['delivery_number'] == plain.delivery_number
        assert plain_dict['utm_coordinates'] == plain.utm_coordinates
        assert plain_dict['observation'] == plain.observation

    def test_create_plain_with_m2m_relations(self):
        client = self.api_client

        projects = ProjectFactory.create_batch(size=3)
        projects_pks = [project.pk for project in projects]

        plain_dict = factory.build(dict, FACTORY_CLASS=PlainFactory, projects=projects_pks)

        response = client.post(reverse('plain-list'), plain_dict)
        created_plain_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED

        plain = Plain.objects.get(pk=created_plain_pk)
        assert projects[0].plains.first().pk == plain.pk
        assert plain.projects.count() == len(projects)

    def test_get_one(self):
        client = self.api_client
        plain_pk = Plain.objects.first().pk
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain_pk})
        response = client.get(plain_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('plain-list'))
        assert response.status_code == status.HTTP_200_OK
        assert Plain.objects.count() == len(response.data)

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        plain_qs = Plain.objects.all()
        plain_count = Plain.objects.count()

        for i, plain in enumerate(plain_qs, start=1):
            response = client.delete(reverse('plain-detail', kwargs={'pk': plain.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert plain_count - i == Plain.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        plain_pk = Plain.objects.first().pk
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain_pk})
        plain_dict = factory.build(dict, FACTORY_CLASS=PlainFactory)
        response = client.patch(plain_detail_url, data=plain_dict)
        assert response.status_code == status.HTTP_200_OK

        assert plain_dict['name'] == response.data['name']
        assert plain_dict['plain_code'] == response.data['plain_code']
        assert plain_dict['customer'] == response.data['customer']
        assert plain_dict['feeder'] == response.data['feeder']
        assert plain_dict['zone'] == response.data['zone']
        assert plain_dict['delivery_number'] == response.data['delivery_number']
        assert plain_dict['utm_coordinates'] == response.data['utm_coordinates']
        assert plain_dict['observation'] == response.data['observation']

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_name = plain.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_name == Plain.objects.first().name

    def test_update_plain_code_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_plain_code = plain.plain_code
        data = {
            'plain_code': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_plain_code == Plain.objects.first().plain_code

    def test_update_customer_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_customer = plain.customer
        data = {
            'customer': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_customer == Plain.objects.first().customer

    def test_update_feeder_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_feeder = plain.feeder
        data = {
            'feeder': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_feeder == Plain.objects.first().feeder

    def test_update_zone_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_zone = plain.zone
        data = {
            'zone': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_zone == Plain.objects.first().zone

    def test_update_delivery_number_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_delivery_number = plain.delivery_number
        data = {
            'delivery_number': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_delivery_number == Plain.objects.first().delivery_number

    def test_update_utm_coordinates_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_utm_coordinates = plain.utm_coordinates
        data = {
            'utm_coordinates': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_utm_coordinates == Plain.objects.first().utm_coordinates

    def test_update_observation_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        plain = Plain.objects.first()
        plain_detail_url = reverse('plain-detail', kwargs={'pk': plain.pk})
        plain_observation = plain.observation
        data = {
            'observation': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(plain_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert plain_observation == Plain.objects.first().observation
