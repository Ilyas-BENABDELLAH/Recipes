# Generated by Django 4.1 on 2022-09-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "recipecategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="recipecategory",
            name="name",
            field=models.CharField(max_length=64),
        ),
    ]
