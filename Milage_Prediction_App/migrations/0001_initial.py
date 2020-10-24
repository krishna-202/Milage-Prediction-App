# Generated by Django 3.0.3 on 2020-10-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MilagePredictionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cylinders', models.IntegerField()),
                ('displacement', models.IntegerField()),
                ('horsepower', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('acceleration', models.IntegerField()),
                ('model_year', models.IntegerField()),
                ('origin', models.IntegerField()),
            ],
        ),
    ]
