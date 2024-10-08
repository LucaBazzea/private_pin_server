# Generated by Django 5.1 on 2024-09-04 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='CircleMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.circle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.user')),
            ],
        ),
    ]
