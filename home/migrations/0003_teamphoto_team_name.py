# Generated by Django 2.1 on 2018-11-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teamphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamphoto',
            name='team_name',
            field=models.CharField(default='BEAST', max_length=50),
            preserve_default=False,
        ),
    ]
