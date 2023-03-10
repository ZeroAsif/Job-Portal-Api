# Generated by Django 4.1.1 on 2022-12-21 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='back_image',
            field=models.ImageField(default='static/user.png', upload_to='static/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='static/user.png', upload_to='static/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
