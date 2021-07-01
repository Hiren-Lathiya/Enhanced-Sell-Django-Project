# Generated by Django 3.2.2 on 2021-06-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compny_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('number', models.CharField(default='', max_length=10)),
                ('address', models.TextField(default='', max_length=200)),
                ('join_date', models.DateField(auto_now=True, null=True)),
                ('profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Profile/')),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
