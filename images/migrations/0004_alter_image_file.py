# Generated by Django 4.2.2 on 2023-06-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_remove_image_path_image_file_image_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.TextField(),
        ),
    ]
