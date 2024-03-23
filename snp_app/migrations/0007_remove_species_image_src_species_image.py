# Generated by Django 4.2 on 2023-05-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snp_app', '0006_alter_sample_sampling_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='image_src',
        ),
        migrations.AddField(
            model_name='species',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]