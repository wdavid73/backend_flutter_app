# Generated by Django 3.1.2 on 2020-11-10 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish_ingredient',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='dish_ingredient',
            name='ingredient',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='Dish_Ingredient',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]