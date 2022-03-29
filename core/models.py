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
        db_table = 'department'
        managed = True

    def __str__(self):
        return self.name

class MaritalStatus(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
        unique=True
    )

    class Meta:
        db_table = 'marital_status'
        managed = True

class State(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
        unique=True
    )
    abreviation = models.CharField(
        null=False,
        max_length=2
    )

    class Meta:
        db_table = 'state'
        managed = True

class City(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
    )
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )

    class Meta:
        db_table = 'city'
        managed = True

class District(ModelBase):
    name = models.CharField(
        null=False,
        max_length=104,
    )
    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False
    )
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )

    class Meta:
        db_table = 'district'
        managed = True

class Employee(ModelBase):

    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    name = models.CharField(
        null=False,
        max_length=104,
    )
    salary = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )
    admission_date = models.DateField(
        null=False
    )
    birthday = models.DateField(
        null=False
    )
    gender = models.CharField(
        null=False,
        max_length=1,
        choices=Gender.choices
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'employee'
        managed = True
