from django.db import models
# from base.models import Base as BaseModel
from auditlog.registry import auditlog

# Create your models here.
class Images():#sBaseModel):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30, null=True, blank=True,
                            unique=True, error_messages={
                                'unique': "This name is already taken."
                                }
                            )
    descriptions = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "images"
        verbose_name_plural = "Images"
        verbose_name = "Image"
        
    def __str__(self):
        return self.name
        
auditlog.register(Images)
