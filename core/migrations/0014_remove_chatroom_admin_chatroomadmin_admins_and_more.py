# Generated by Django 4.1.2 on 2022-12-07 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_user_profile_privatechat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom_admin',
            name='chatroomAdmin_admins',
        ),
        migrations.RemoveField(
            model_name='chatroom_admin',
            name='chatroomAdmin_chatroom_id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_users',
        ),
        migrations.RemoveField(
            model_name='group_admin_user',
            name='groupAdminUser_chatroom_id',
        ),
        migrations.RemoveField(
            model_name='group_admin_user',
            name='groupAdminUser_owner',
        ),
        migrations.RemoveField(
            model_name='privatechat',
            name='privatechatTo_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_chatroom',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_group',
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
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='ChatRoom_Admin',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Group_Admin_User',
        ),
        migrations.DeleteModel(
            name='PrivateChat',
        ),
    ]
