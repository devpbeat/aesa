import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Project
from .factories import PlainFactory, ProjectFactory

faker = Factory.create()


class Project_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        ProjectFactory.create_batch(size=3)

    def test_create_project(self):
        """
        Ensure we can create a new project object.
        """
        client = self.api_client
        project_count = Project.objects.count()
        project_dict = factory.build(dict, FACTORY_CLASS=ProjectFactory)
        response = client.post(reverse('project-list'), project_dict)
        created_project_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert Project.objects.count() == project_count + 1
        project = Project.objects.get(pk=created_project_pk)

        assert project_dict['name'] == project.name
        assert project_dict['ruc'] == project.ruc
        assert project_dict['social_reason'] == project.social_reason

    def test_create_project_with_m2m_relations(self):
        client = self.api_client

        plains = PlainFactory.create_batch(size=3)
        plains_pks = [plain.pk for plain in plains]

        project_dict = factory.build(dict, FACTORY_CLASS=ProjectFactory, plains=plains_pks)

        response = client.post(reverse('project-list'), project_dict)
        created_project_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED

        project = Project.objects.get(pk=created_project_pk)
        assert plains[0].projects.first().pk == project.pk
        assert project.plains.count() == len(plains)

    def test_get_one(self):
        client = self.api_client
        project_pk = Project.objects.first().pk
        project_detail_url = reverse('project-detail', kwargs={'pk': project_pk})
        response = client.get(project_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('project-list'))
        assert response.status_code == status.HTTP_200_OK
        assert Project.objects.count() == len(response.data)

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        project_qs = Project.objects.all()
        project_count = Project.objects.count()

        for i, project in enumerate(project_qs, start=1):
            response = client.delete(reverse('project-detail', kwargs={'pk': project.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert project_count - i == Project.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        project_pk = Project.objects.first().pk
        project_detail_url = reverse('project-detail', kwargs={'pk': project_pk})
        project_dict = factory.build(dict, FACTORY_CLASS=ProjectFactory)
        response = client.patch(project_detail_url, data=project_dict)
        assert response.status_code == status.HTTP_200_OK

        assert project_dict['name'] == response.data['name']
        assert project_dict['ruc'] == response.data['ruc']
        assert project_dict['social_reason'] == response.data['social_reason']

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        project = Project.objects.first()
        project_detail_url = reverse('project-detail', kwargs={'pk': project.pk})
        project_name = project.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(project_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert project_name == Project.objects.first().name

    def test_update_ruc_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        project = Project.objects.first()
        project_detail_url = reverse('project-detail', kwargs={'pk': project.pk})
        project_ruc = project.ruc
        data = {
            'ruc': faker.pystr(min_chars=21, max_chars=21),
        }
        response = client.patch(project_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert project_ruc == Project.objects.first().ruc

    def test_update_social_reason_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        project = Project.objects.first()
        project_detail_url = reverse('project-detail', kwargs={'pk': project.pk})
        project_social_reason = project.social_reason
        data = {
            'social_reason': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(project_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert project_social_reason == Project.objects.first().social_reason
