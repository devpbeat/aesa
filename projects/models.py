from django.db import models
from plains.models import Plain
from base.models import Base as BaseModel
from auditlog.registry import auditlog

# Create your models here.

class Project(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)
    project_code = models.CharField(max_length=255, null=False, blank=False, unique=True)
    plains = models.ManyToManyField(
        Plain, related_name="projects", db_table="project_plain", blank=True
    )

    class Meta:
        db_table = "project"
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.name
    
auditlog.register(Project)
