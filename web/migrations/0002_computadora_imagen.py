# Generated by Django 5.1.1 on 2024-10-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='computadoras/'),
        ),
    ]
