# Generated by Django 3.2.9 on 2022-06-14 10:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItemsModel',
            fields=[
                ('ordered_items_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('created_by', models.IntegerField(default=1)),
                ('deleted', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.itemmodel')),
            ],
            options={
                'db_table': 'ordered_items',
            },
        ),
    ]
