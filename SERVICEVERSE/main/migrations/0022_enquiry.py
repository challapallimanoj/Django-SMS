# Generated by Django 3.1.4 on 2021-05-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_carpentering_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('supervisor', models.CharField(max_length=200)),
            ],
        ),
    ]