# Generated by Django 2.2.5 on 2019-11-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField(default=False)),
                ('topic', models.CharField(max_length=32)),
                ('last_message', models.TextField()),
            ],
        ),
    ]
