# Generated by Django 3.2.6 on 2021-09-04 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0028_alter_unit_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_bars', models.BooleanField(default=True, help_text='Displays the level bars on the main portal', verbose_name='Level bars')),
                ('show_completed_by_default', models.BooleanField(default=True, help_text='Displays completed units on the main portal by default', verbose_name='Show completed')),
                ('show_locked_by_default', models.BooleanField(default=True, help_text='Displays locked units on the main portal by default', verbose_name='Show locked')),
                ('user', models.OneToOneField(help_text='The user these preferences belong to', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]