# Generated by Django 4.2.2 on 2023-06-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
