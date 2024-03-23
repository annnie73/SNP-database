# Generated by Django 4.2 on 2023-06-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snp_app', '0008_alter_animal_id_alter_animal_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snp',
            name='species',
        ),
        migrations.AddField(
            model_name='snp',
            name='sample',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snp_app.sample'),
            preserve_default=False,
        ),
    ]
