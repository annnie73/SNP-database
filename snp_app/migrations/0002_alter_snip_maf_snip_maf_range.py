# Generated by Django 4.2 on 2023-05-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snip',
            name='MAF',
            field=models.FloatField(),
        ),
        migrations.AddConstraint(
            model_name='snip',
            constraint=models.CheckConstraint(check=models.Q(('MAF__gte', 0.0), ('MAF__lte', 1.0)), name='MAF_range'),
        ),
    ]
