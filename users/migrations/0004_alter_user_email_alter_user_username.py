# Generated by Django 4.2.14 on 2024-08-16 06:03

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 사용 중인 아이디입니다.'}, max_length=20, unique=True, validators=[users.models.validate_username]),
        ),
    ]