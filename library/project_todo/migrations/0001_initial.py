# Generated by Django 4.0.4 on 2022-05-31 11:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='NONAME project', max_length=64, verbose_name="project's name")),
                ('repo_link', models.URLField(default=uuid.uuid4, verbose_name='repo link here')),
                ('users_list', models.ManyToManyField(to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='None note', max_length=128, verbose_name='note text')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_updated', models.DateTimeField(default=datetime.datetime.now)),
                ('note_creator', models.ManyToManyField(to='users.user')),
                ('project_name_todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_todo.project')),
            ],
        ),
    ]
