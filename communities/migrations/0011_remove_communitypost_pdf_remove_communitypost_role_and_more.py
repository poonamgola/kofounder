# Generated by Django 4.2 on 2024-07-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0010_addmyproject_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitypost',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='communitypost',
            name='role',
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='sector',
            field=models.CharField(default='default_sector', max_length=100, verbose_name='sector'),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='sub_sector',
            field=models.CharField(default='sub_sector', max_length=100, verbose_name='sub_sector'),
        ),
        migrations.DeleteModel(
            name='AddMyProject',
        ),
    ]