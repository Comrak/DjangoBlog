# Generated by Django 5.0.6 on 2024-07-01 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_tag_alter_post_options_post_likes_alter_post_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="etiqueta",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
