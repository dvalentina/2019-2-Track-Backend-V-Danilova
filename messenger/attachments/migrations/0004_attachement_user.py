# Generated by Django 2.2.5 on 2019-11-19 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attachments', '0003_attachement_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь, создавший вложение'),
        ),
    ]