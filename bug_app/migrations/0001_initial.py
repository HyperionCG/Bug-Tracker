# Generated by Django 3.0.6 on 2020-05-25 01:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]