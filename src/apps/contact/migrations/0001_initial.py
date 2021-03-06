# Generated by Django 2.0.4 on 2018-04-23 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create at')),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Update at')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Asunto')),
                ('text', models.TextField(verbose_name='Mensaje')),
                ('is_register', models.BooleanField(verbose_name='Usuario registrado')),
                ('has_read', models.BooleanField(default=False, verbose_name='Mensaje leído')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
