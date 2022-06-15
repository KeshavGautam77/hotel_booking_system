# Generated by Django 3.2 on 2021-05-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0008_auto_20210510_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='db.sqlite3')),
            ],
        ),
    ]