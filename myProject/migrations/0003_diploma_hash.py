# Generated by Django 4.1.7 on 2023-04-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0002_rename_luogonascita_diploma_luogonascita'),
    ]

    operations = [
        migrations.AddField(
            model_name='diploma',
            name='hash',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]
