# Generated by Django 4.2 on 2024-07-15 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_billing_updated_at_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 340910)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='billing_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 339744)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 338198)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 337791)),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 340563)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 339325)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 336492)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 335900)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='will_expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 335918)),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 338918)),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 338524)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 336819)),
        ),
        migrations.AlterField(
            model_name='twofactorverification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 25, 7, 336228)),
        ),
    ]
