from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from aesa.serializers import ProjectSerializer

from .factories import ProjectFactory


class ProjectSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.project = ProjectFactory.create()

    def test_that_a_project_is_correctly_serialized(self):
        project = self.project
        serializer = ProjectSerializer
        serialized_project = serializer(project).data

        assert serialized_project['id'] == project.id
        assert serialized_project['name'] == project.name
        assert serialized_project['ruc'] == project.ruc
        assert serialized_project['social_reason'] == project.social_reason
