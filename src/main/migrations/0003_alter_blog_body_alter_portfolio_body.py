# Generated by Django 4.1.1 on 2022-09-17 17:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
