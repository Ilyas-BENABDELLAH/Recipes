# Generated by Django 4.1 on 2022-09-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "alter_recipecategory_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="recipes/"),
        ),
    ]
