# Generated by Django 3.2.4 on 2021-09-26 14:37

import api_admin.Dish.models.DishModel
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(default='not-image.png', upload_to=api_admin.Dish.models.DishModel.nameFile),
        ),
    ]
