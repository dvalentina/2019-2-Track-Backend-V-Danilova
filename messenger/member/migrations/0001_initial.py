# Generated by Django 2.2.5 on 2019-11-07 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('chat', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_messages', models.IntegerField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.Chat')),
                ('last_read_message', models.ManyToManyField(to='message.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
        ),
    ]