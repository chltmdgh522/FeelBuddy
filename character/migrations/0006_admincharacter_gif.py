# Generated by Django 5.0.8 on 2024-08-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_usercharacter_last_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincharacter',
            name='gif',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]