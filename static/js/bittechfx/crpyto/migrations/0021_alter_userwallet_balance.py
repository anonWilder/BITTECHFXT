# Generated by Django 3.2.8 on 2021-12-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crpyto', '0020_alter_usermembership_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='balance',
            field=models.FloatField(),
        ),
    ]
