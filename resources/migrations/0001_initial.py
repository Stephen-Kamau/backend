# Generated by Django 3.1.3 on 2021-06-13 11:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_user_password_reset_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=500, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('unitname', models.CharField(blank=True, max_length=30, verbose_name='unit name')),
                ('year', models.CharField(blank=True, max_length=30, verbose_name='year of unit')),
                ('course', models.CharField(blank=True, max_length=30, verbose_name='course name')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'db_table': 'CIT_RESOURCE_TABLE',
            },
        ),
    ]
