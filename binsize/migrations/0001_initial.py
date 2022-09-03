# Generated by Django 3.1.14 on 2022-08-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_size', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('bin_size_w', models.FloatField(default=0, verbose_name='Bin Width')),
                ('bin_size_d', models.FloatField(default=0, verbose_name='Bin Depth')),
                ('bin_size_h', models.FloatField(default=0, verbose_name='Bin Height')),
                ('creater', models.CharField(max_length=255, verbose_name='Who created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Bin Size',
                'verbose_name_plural': 'Bin Size',
                'db_table': 'binsize',
                'ordering': ['-id'],
            },
        ),
    ]
