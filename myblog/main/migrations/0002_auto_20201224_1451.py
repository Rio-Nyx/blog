# Generated by Django 3.1.4 on 2020-12-24 14:51

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
