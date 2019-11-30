# Generated by Django 2.2.6 on 2019-10-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=10)),
                ('intro', models.TextField()),
            ],
        ),
    ]
