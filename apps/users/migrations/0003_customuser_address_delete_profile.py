# Generated by Django 4.2.17 on 2024-12-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_role_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
