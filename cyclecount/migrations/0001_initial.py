# Generated by Django 3.1.14 on 2022-08-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CyclecountModeDayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('cyclecount_status', models.IntegerField(default=0, verbose_name='Cycle Count Status')),
                ('bin_name', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_qty', models.BigIntegerField(default=0, verbose_name='On Hand Stock')),
                ('physical_inventory', models.BigIntegerField(default=0, verbose_name='Goods Code')),
                ('difference', models.BigIntegerField(default=0, verbose_name='Goods Code')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Create')),
                ('t_code', models.CharField(max_length=255, verbose_name='Transaction Code')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Cyclecount Day',
                'verbose_name_plural': 'Cyclecount Day',
                'db_table': 'cyclecountday',
                'ordering': ['openid'],
            },
        ),
        migrations.CreateModel(
            name='QTYRecorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('mode_code', models.CharField(max_length=255, verbose_name='Transaction Mode')),
                ('bin_name', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_qty', models.BigIntegerField(default=0, verbose_name='On Hand Stock')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Create')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'QTY Recorder',
                'verbose_name_plural': 'QTY Recorder',
                'db_table': 'qtyrecorder',
                'ordering': ['-id'],
            },
        ),
    ]
