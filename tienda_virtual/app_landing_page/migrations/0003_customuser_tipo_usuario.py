# Generated by Django 4.2.4 on 2023-08-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing_page', '0002_alter_customuser_email_alter_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]