# Generated by Django 4.2.7 on 2024-07-26 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_stock_user_current_and_yesterday_money_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_user',
            name='count_for_days',
        ),
    ]