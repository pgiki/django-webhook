# Generated by Django 5.0.7 on 2024-11-26 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_webhook', '0007_remove_webhooktopic_permissions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webhooktopic',
            old_name='permissions_required',
            new_name='permissions',
        ),
    ]
