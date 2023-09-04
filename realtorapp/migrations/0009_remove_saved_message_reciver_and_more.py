# Generated by Django 4.2.4 on 2023-08-25 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtorapp', '0008_saved_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saved_message',
            name='reciver',
        ),
        migrations.AlterField(
            model_name='saved_message',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='saved_message',
            name='reciver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to=settings.AUTH_USER_MODEL),
        ),
    ]
