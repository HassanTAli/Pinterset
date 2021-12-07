# Generated by Django 3.2.9 on 2021-11-24 11:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0004_alter_pin_reactees'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='save',
            options={'ordering': ['-saved_at']},
        ),
        migrations.AlterUniqueTogether(
            name='history',
            unique_together={('user', 'pin')},
        ),
        migrations.AlterUniqueTogether(
            name='save',
            unique_together={('user', 'pin')},
        ),
    ]