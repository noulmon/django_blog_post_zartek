# Generated by Django 3.0.5 on 2020-04-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_postimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'post_image', 'verbose_name_plural': 'post_images'},
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='uploads/images/<django.db.models.fields.related_descriptors.ForwardManyToOneDescriptor object at 0x0000014819393B08>'),
        ),
        migrations.AlterModelTable(
            name='postimage',
            table='POST_IMAGE',
        ),
    ]
