# Generated by Django 4.2 on 2024-07-14 06:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, max_length=255, null=True)),
                ('request_method', models.CharField(blank=True, max_length=255, null=True)),
                ('request_headers', models.TextField(blank=True, null=True)),
                ('request_parameters', models.CharField(blank=True, max_length=255, null=True)),
                ('request_body', models.TextField(blank=True, null=True)),
                ('client_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('view_name', models.CharField(blank=True, max_length=255, null=True)),
                ('response_status_code', models.CharField(blank=True, max_length=255, null=True)),
                ('environment', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 236388))),
                ('response_content', models.TextField(blank=True, null=True)),
                ('request_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=1000, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('referer', models.URLField(blank=True, max_length=2000, null=True)),
                ('request_query_params', models.JSONField(blank=True, null=True)),
                ('response_headers', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('registered_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 233831))),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('uid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('error_message', models.TextField()),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, max_length=255, null=True)),
                ('request_method', models.CharField(blank=True, max_length=255, null=True)),
                ('request_headers', models.TextField(blank=True, null=True)),
                ('request_parameters', models.CharField(blank=True, max_length=255, null=True)),
                ('request_body', models.TextField(blank=True, null=True)),
                ('client_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('stack_trace', models.TextField()),
                ('exception_type', models.CharField(blank=True, max_length=255, null=True)),
                ('view_name', models.CharField(blank=True, max_length=255, null=True)),
                ('response_status_code', models.CharField(blank=True, max_length=255, null=True)),
                ('enviroment', models.CharField(blank=True, max_length=255, null=True)),
                ('error_location', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 235909))),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('registered_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 232202))),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 231723))),
                ('will_expire_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 231746))),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=255, unique=True)),
                ('password', models.TextField()),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 232561))),
                ('is_active', models.BooleanField(default=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_roles', to='app.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dicount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('is_available', models.BooleanField(default=1)),
                ('is_active', models.BooleanField(default=1)),
                ('added_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 234336))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_product', to='app.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_payment_modes', to='app.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255, unique=True)),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 234806))),
                ('is_active', models.BooleanField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_order', to='app.customer')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_order', to='app.organization')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_order', to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.TextField()),
                ('registered_at', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 233343))),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_employee', to='app.organization')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_role', to='app.role')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_customer', to='app.organization'),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=255, unique=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('billing_date', models.DateTimeField(default=datetime.datetime(2024, 7, 14, 12, 3, 16, 235342))),
                ('is_active', models.BooleanField(default=1)),
                ('billed_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_billing', to='app.employee')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_billing', to='app.customer')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_billing', to='app.organization')),
                ('payment_mode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymode_billing', to='app.paymentmode')),
            ],
        ),
    ]
