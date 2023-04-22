from django.db import models


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    ruc = models.CharField(max_length=20, unique=True)
    social_reason = models.CharField(max_length=255, null=True, blank=True)
    plains = models.ManyToManyField('Plain', related_name='projects',
                                    db_table='project_plain', blank=True)

    class Meta:
        db_table = "project"


class Plain(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    plain_code = models.CharField(max_length=255, null=True, blank=True, unique=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    feeder = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=255, null=True, blank=True)
    delivery_number = models.CharField(max_length=255, null=True, blank=True)
    utm_coordinates = models.CharField(max_length=255, null=True, blank=True)
    observation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "plain"
