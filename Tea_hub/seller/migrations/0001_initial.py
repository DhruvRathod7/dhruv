# Generated by Django 3.2.9 on 2022-06-11 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerModel',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(default='', max_length=100)),
                ('mobile_no', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('created_by', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]
