# Generated by Django 4.2.4 on 2023-09-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=256, upload_to='uploads/'),
        ),
    ]
