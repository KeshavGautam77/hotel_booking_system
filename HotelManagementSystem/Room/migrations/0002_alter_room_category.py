# Generated by Django 3.2 on 2021-04-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('QUE', 'QUEEN'), ('KIN', 'KING'), ('YAC', 'AC')], max_length=3),
        ),
    ]
