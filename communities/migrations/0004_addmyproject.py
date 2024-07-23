# Generated by Django 4.2 on 2024-07-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_remove_communitypost_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100, null=True)),
                ('sector', models.CharField(max_length=100, null=True)),
                ('sub_sector', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
        ),
    ]
