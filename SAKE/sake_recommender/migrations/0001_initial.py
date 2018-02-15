# Generated by Django 2.0.2 on 2018-02-15 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=128)),
                ('producing_area', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('urls', models.URLField(blank=True, null=True)),
            ],
        ),
    ]