# Generated by Django 2.2.3 on 2019-08-30 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_mainte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_staff',
            name='authuser_id',
            field=models.ForeignKey(db_column='authuser_id', default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='NSYSユーザーID'),
        ),
    ]
