# Generated by Django 5.0.4 on 2024-04-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField()),
            ],
        ),
    ]