# Generated by Django 3.2 on 2021-04-20 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(null=True)),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.airports')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights.airports')),
            ],
        ),
    ]
