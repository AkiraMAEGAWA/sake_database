# Generated by Django 2.0.2 on 2018-02-15 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sake_recommender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sake',
            old_name='type',
            new_name='_type',
        ),
    ]
