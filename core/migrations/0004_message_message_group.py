# Generated by Django 4.1.2 on 2022-12-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_group_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.group'),
        ),
    ]
