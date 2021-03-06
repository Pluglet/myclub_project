# Generated by Django 3.2 on 2021-04-27 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='event',
            managers=[
                ('events', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='venue',
            managers=[
                ('venues', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
