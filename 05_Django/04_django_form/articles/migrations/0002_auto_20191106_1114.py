# Generated by Django 2.2.6 on 2019-11-06 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
