# Generated by Django 4.2 on 2024-07-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0007_alter_addmyproject_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmyproject',
            name='description',
            field=models.TextField(),
        ),
    ]
