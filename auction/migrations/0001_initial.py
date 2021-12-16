# Generated by Django 4.0 on 2021-12-16 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=40)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('duration_type', models.CharField(choices=[('Short', 'short'), ('Medium', 'medium'), ('Long', 'long')], max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customuser')),
            ],
            options={
                'verbose_name': 'Auction',
                'verbose_name_plural': 'Auctions',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customuser')),
            ],
            options={
                'verbose_name': 'Bid',
                'verbose_name_plural': 'Bids',
            },
        ),
    ]
