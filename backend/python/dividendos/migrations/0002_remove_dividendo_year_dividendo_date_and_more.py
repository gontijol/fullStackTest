# Generated by Django 4.2.5 on 2023-10-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividendos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dividendo',
            name='year',
        ),
        migrations.AddField(
            model_name='dividendo',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='dividendo',
            name='symbol',
            field=models.CharField(max_length=255),
        ),
    ]
