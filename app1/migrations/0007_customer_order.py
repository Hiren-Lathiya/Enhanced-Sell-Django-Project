# Generated by Django 3.2.2 on 2021-06-15 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_compny_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveBigIntegerField(default=0)),
                ('total_price', models.PositiveBigIntegerField(default=0)),
                ('order_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.compny_details')),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.compny_customers')),
                ('prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.compny_products')),
            ],
        ),
    ]
