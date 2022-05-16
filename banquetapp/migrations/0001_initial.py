# Generated by Django 4.0.1 on 2022-04-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetailsModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter FullName', max_length=100)),
                ('email', models.EmailField(help_text='Enter Email id', max_length=100)),
                ('contact', models.BigIntegerField(help_text='Enter Mobile Number', null=True)),
                ('password', models.CharField(help_text='Enter Password', max_length=100)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]