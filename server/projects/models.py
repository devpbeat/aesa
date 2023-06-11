from django.db import models
from plains.models import Plain
# from base.models import Base as BaseModel
from auditlog.registry import auditlog

# Create your models here.

class Project():#BaseModel):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)
    project_code = models.CharField(max_length=255, null=False, blank=False, unique=True)

    class Meta:
        db_table = "project"
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.name
    
auditlog.register(Project)

class ProjectPlains():#BaseModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    plain = models.ForeignKey(Plain, on_delete=models.PROTECT)

    class Meta:
        db_table = "project_plains"
        verbose_name_plural = "Project Plains"
        verbose_name = "Project Plain"

    def __str__(self):
        return self.project.name + " - " + self.plain.name
    
auditlog.register(ProjectPlains)

