# Generated by Django 5.1.3 on 2024-12-19 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlacakVerecek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kişi', models.CharField(max_length=255)),
                ('tür', models.CharField(choices=[('ALACAK', 'Alacak'), ('BORÇ', 'Borç')], max_length=10)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('son_odeme_tarihi', models.DateField()),
                ('durum', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, verbose_name='Kasa Adı')),
                ('bakiye', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Bakiye')),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('tür', models.CharField(choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tür', models.CharField(choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')], max_length=10)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tarih', models.DateField()),
                ('açıklama', models.TextField(blank=True, null=True)),
                ('kasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.kasa', verbose_name='Kasa')),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numara', models.CharField(max_length=50, unique=True)),
                ('müşteri', models.CharField(max_length=255)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tarih', models.DateField()),
                ('kdv_oranı', models.DecimalField(decimal_places=2, default=18, max_digits=5)),
                ('kasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.kasa', verbose_name='Kasa')),
            ],
        ),
        migrations.CreateModel(
            name='CekSenet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tür', models.CharField(choices=[('ÇEK', 'Çek'), ('SENET', 'Senet')], max_length=10)),
                ('numara', models.CharField(max_length=50)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tarih', models.DateField(verbose_name='Senet Tarihi')),
                ('durum', models.BooleanField(default=False)),
                ('kasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.kasa', verbose_name='Kasa')),
            ],
        ),
        migrations.CreateModel(
            name='KasaHareketi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('işlem_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='İşlem Tarihi')),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tutar')),
                ('açıklama', models.CharField(blank=True, max_length=255, verbose_name='Açıklama')),
                ('tür', models.CharField(choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')], max_length=10, verbose_name='Tür')),
                ('kasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.kasa', verbose_name='Kasa')),
            ],
        ),
        migrations.CreateModel(
            name='GelirGider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tür', models.CharField(choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')], max_length=10)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('açıklama', models.TextField(blank=True, null=True)),
                ('tarih', models.DateField(auto_now_add=True)),
                ('kasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.kasa', verbose_name='Kasa')),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Veresiye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kişi', models.CharField(max_length=255)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('son_odeme_tarihi', models.DateField()),
                ('durum', models.BooleanField(default=False)),
                ('alacak_verecek', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.alacakverecek')),
            ],
        ),
    ]
