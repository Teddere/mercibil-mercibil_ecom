# Generated by Django 5.1 on 2024-08-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile/profile_no.svg', upload_to='profile/'),
        ),
    ]
