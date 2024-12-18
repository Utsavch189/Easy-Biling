# Generated by Django 4.2 on 2024-07-20 02:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_cgst_billing_cgst_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 577915)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='billing_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 576425)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 574119)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 573601)),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 577494)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 575593)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 571946)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 571213)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='will_expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 571234)),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 575094)),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 574564)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 572346)),
        ),
        migrations.AlterField(
            model_name='twofactorverification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 8, 29, 8, 571613)),
        ),
    ]
