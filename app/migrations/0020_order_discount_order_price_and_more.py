# Generated by Django 4.2 on 2024-07-26 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_billing_invoice_path_alter_accesslog_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 353044)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='billing_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 351555)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 349156)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 348626)),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 352637)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 350680)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 346953)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 346236)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='will_expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 346255)),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 350161)),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 349696)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 347389)),
        ),
        migrations.AlterField(
            model_name='twofactorverification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 26, 9, 58, 18, 346626)),
        ),
    ]
