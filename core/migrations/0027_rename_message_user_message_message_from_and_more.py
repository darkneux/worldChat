# Generated by Django 4.1.2 on 2022-12-07 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_remove_user_profile_privatechat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_user',
            new_name='message_from',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_privatchat',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='privatechat',
        ),
        migrations.DeleteModel(
            name='PrivateChat',
        ),
    ]
