# Generated by Django 4.0.3 on 2022-03-30 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_branch_customer_product_productgroup_sale_supplier_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='abreviation',
            new_name='abbreviation',
        ),
    ]
