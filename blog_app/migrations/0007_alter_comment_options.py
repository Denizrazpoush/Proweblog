# Generated by Django 4.0.4 on 2022-07-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
    ]