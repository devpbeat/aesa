from django.db import models
from images.models import Images
from base.models import Base as BaseModel
from auditlog.registry import auditlog

# Create your models here.
class Plain(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    plain_code = models.CharField(max_length=255, null=False, blank=False, unique=True)
    feeder = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=255, null=True, blank=True)
    delivery_number = models.CharField(max_length=255, null=True, blank=True)
    utm_coordinates = models.CharField(max_length=255, null=True, blank=True)
    observation = models.CharField(max_length=255, null=True, blank=True)
    images = models.ManyToManyField(
        "images.Images", related_name="plains", db_table="plain_image", blank=True
    )
    
    class Meta:
        db_table = "plain"
        verbose_name_plural = "Plains"
        verbose_name = "Plain"
    
    def __str__(self):
        return self.name


auditlog.register(Plain)

