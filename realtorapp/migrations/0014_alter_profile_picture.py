# Generated by Django 3.2.23 on 2024-03-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtorapp', '0013_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, default='static/login/images/user/0.jpg', null=True, upload_to='media'),
        ),
    ]
