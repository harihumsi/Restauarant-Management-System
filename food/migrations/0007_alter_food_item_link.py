# Generated by Django 5.0.4 on 2024-04-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_food_item_delete_food_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_item',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]