# Generated by Django 2.2.5 on 2019-11-28 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='last_read_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='message.Message', verbose_name='последнее прочитанное сообщение'),
        ),
        migrations.AlterField(
            model_name='member',
            name='new_messages',
            field=models.IntegerField(verbose_name='количество новых сообщений'),
        ),
    ]