# Generated by Django 3.1 on 2021-06-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0002_auto_20210618_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
    ]
