# Generated by Django 4.1 on 2022-09-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "recipeingredient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="amount",
            field=models.CharField(max_length=32),
        ),
    ]
