# Generated by Django 4.1.2 on 2022-12-07 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_remove_chatroom_admin_chatroomadmin_admins_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('chatroom_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('chatroom_name', models.CharField(max_length=16, unique=True)),
                ('chatroom_passwd', models.CharField(max_length=32)),
                ('chatroom_about', models.CharField(default='', max_length=96)),
                ('chatroom_createTime', models.DateTimeField(auto_now_add=True)),
                ('chatroom_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
