# Generated by Django 4.0.3 on 2022-03-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=104)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=104)),
                ('city', models.ForeignKey(db_column='id_city', on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
                ('zone', models.ForeignKey(db_column='id_zone', on_delete=django.db.models.deletion.DO_NOTHING, to='core.zone')),
            ],
            options={
                'db_table': 'district',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=104, unique=True)),
            ],
            options={
                'db_table': 'marital_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=104, unique=True)),
                ('abreviation', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'state',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=104)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=16)),
                ('admission_date', models.DateField()),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('department', models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.DO_NOTHING, to='core.department')),
                ('district', models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district')),
                ('marital_status', models.ForeignKey(db_column='id_marital_status', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maritalstatus')),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, to='core.state'),
        ),
    ]