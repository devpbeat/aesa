from django.db import models
from projects.models import *
from base.models import Base as BaseModel
from auditlog.registry import auditlog

# Create your models here.
class Customer(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    ruc = models.CharField(max_length=20, unique=True)
    social_reason = models.CharField(max_length=255, null=False, blank=False)
    projects = models.ManyToManyField(
        Project, related_name="customers", db_table="customer_project", blank=True
    )

    class Meta:
        db_table = "customer"
        verbose_name_plural = "Customers"
        verbose_name = "Customer"
    
    def __str__(self):
        return self.name
    

auditlog.register(Customer)