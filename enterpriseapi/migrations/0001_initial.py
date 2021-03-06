# Generated by Django 3.1.7 on 2021-03-30 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Nit', models.BigIntegerField()),
                ('Gln', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterpriseapi.enterprise')),
            ],
        ),
    ]
