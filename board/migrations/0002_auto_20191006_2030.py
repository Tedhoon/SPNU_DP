# Generated by Django 2.1.8 on 2019-10-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeboard',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
