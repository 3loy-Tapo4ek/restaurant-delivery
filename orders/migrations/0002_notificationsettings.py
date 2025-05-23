# Generated by Django 5.2 on 2025-04-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email для уведомлений')),
                ('telegram_token', models.CharField(max_length=200, verbose_name='Telegram Bot Token')),
                ('telegram_chat_id', models.CharField(max_length=100, verbose_name='Telegram Chat ID')),
            ],
            options={
                'verbose_name': 'Настройки уведомлений',
                'verbose_name_plural': 'Настройки уведомлений',
            },
        ),
    ]
