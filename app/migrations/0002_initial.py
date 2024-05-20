# Generated by Django 5.0.3 on 2024-05-15 03:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedfor',
            name='applicants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatbox',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cont_reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatbox',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cont_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chatbox'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postings',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appliedfor',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postings'),
        ),
    ]
