# Generated by Django 4.1.1 on 2022-09-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_portfolio_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactprofile',
            name='has_been_viewed',
            field=models.BooleanField(default=False),
        ),
    ]
