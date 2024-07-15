# Generated by Django 4.2 on 2024-07-15 07:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_twofactorverification_alter_accesslog_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='orders',
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 77797)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='billing_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 76662)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 75475)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 75062)),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 77404)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 76258)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 73820)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 73232)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='will_expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 73249)),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 75829)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 74129)),
        ),
        migrations.AlterField(
            model_name='role',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_roles', to='app.organization'),
        ),
        migrations.AlterField(
            model_name='systemadmin',
            name='role',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='twofactorverification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 13, 14, 40, 73550)),
        ),
        migrations.CreateModel(
            name='OrderMapToBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_mapping', to='app.billing')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_mapping', to='app.order')),
            ],
        ),
    ]