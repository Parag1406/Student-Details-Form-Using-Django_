# Generated by Django 4.0.3 on 2023-03-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sem', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]