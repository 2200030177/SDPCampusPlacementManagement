# Generated by Django 5.0.4 on 2024-04-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
    ]
