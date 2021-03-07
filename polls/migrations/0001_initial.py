# Generated by Django 3.1.1 on 2021-03-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rname', models.CharField(max_length=255)),
                ('RPhone', models.CharField(max_length=32)),
                ('RCIN', models.IntegerField()),
                ('RAddress', models.TextField()),
                ('RCountry', models.CharField(max_length=255)),
                ('ShopkeeperName', models.CharField(max_length=255)),
                ('CommissionGivingAmt', models.DecimalField(decimal_places=4, max_digits=16)),
                ('TotalSalesAmt', models.DecimalField(decimal_places=2, max_digits=16)),
                ('ContactEmail', models.EmailField(max_length=254)),
                ('ProductDetails', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.BooleanField(default=False)),
                ('TransactionStatus', models.BooleanField(default=True)),
            ],
        ),
    ]
