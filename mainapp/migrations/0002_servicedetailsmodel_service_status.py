# Generated by Django 4.0.1 on 2022-04-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetailsmodel',
            name='service_status',
            field=models.CharField(help_text='Enter Email id', max_length=100, null=True),
        ),
    ]
