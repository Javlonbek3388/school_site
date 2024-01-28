# Generated by Django 4.2.7 on 2023-12-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0003_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_org',
            field=models.CharField(choices=[('1', 'Parlament'), ('5', 'Boshqarma'), ('2', 'Prezident'), ('4', 'Xalq talimi vazirligi'), ('3', 'Vazirlar mahkamasi')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('3', 'Farmoyish'), ('4', 'Buyruq'), ('2', 'Qaror'), ('5', 'Farmon'), ('1', 'Qonun')], max_length=15, verbose_name='Toifa/Type'),
        ),
    ]