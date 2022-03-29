from django.db import models

class ModelBase(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )
    active = models.BooleanField(
        default=True
    )
    class Meta:
        abstract = True

class Zone(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
        unique=True
    )

    class Meta:
        db_table = 'zone'
        managed = True

class Department(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
        unique=True
    )

    class Meta:
        db_table = 'departament'
        managed = True
