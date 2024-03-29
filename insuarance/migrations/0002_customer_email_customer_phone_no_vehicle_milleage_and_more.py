# Generated by Django 5.0.1 on 2024-01-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insuarance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="phone_no",
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="milleage",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vehicle",
            name="type",
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
