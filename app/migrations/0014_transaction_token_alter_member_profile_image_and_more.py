# Generated by Django 4.2.6 on 2024-02-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_successfultransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='token',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_image',
            field=models.ImageField(blank=True, default='member/avatar-profile_n68t05.jpg', null=True, upload_to='member/'),
        ),
        migrations.AlterField(
            model_name='mitra',
            name='profile_image',
            field=models.ImageField(blank=True, default='mitra/default-logo_sicqfg.png', null=True, upload_to='mitra/'),
        ),
    ]