# Generated by Django 4.2 on 2024-07-17 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_producttype_organization_alter_accesslog_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 909547)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='billing_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 908388)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 906733)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 906327)),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 909211)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 907958)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 905032)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 904441)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='will_expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 904459)),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 907551)),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 907119)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 905354)),
        ),
        migrations.AlterField(
            model_name='twofactorverification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 21, 59, 57, 904767)),
        ),
    ]
