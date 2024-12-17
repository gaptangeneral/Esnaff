# Generated by Django 5.1.3 on 2024-12-15 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ad')),
                ('last_name', models.CharField(max_length=100, verbose_name='Soyad')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-posta')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon')),
                ('department', models.CharField(max_length=100, verbose_name='Departman')),
                ('position', models.CharField(max_length=100, verbose_name='Pozisyon')),
                ('salary_amount', models.DecimalField(decimal_places=2, default=1000, max_digits=10, verbose_name='Maaş')),
                ('hire_date', models.DateField(verbose_name='İşe Başlama Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi')),
                ('gender', models.CharField(choices=[('MALE', 'Erkek'), ('FEMALE', 'Kadın'), ('OTHER', 'Diğer')], default='', max_length=10, verbose_name='Cinsiyet')),
                ('tckn', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='T.C. Kimlik No')),
                ('sgk_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='SGK No')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi')),
                ('employee_type', models.CharField(choices=[('FULLTIME', 'Tam Zamanlı'), ('PARTTIME', 'Yarı Zamanlı'), ('CONTRACT', 'Sözleşmeli'), ('INTERN', 'Stajyer')], default='FULLTIME', max_length=20, verbose_name='Çalışma Tipi')),
            ],
            options={
                'verbose_name': 'Çalışan',
                'verbose_name_plural': 'Çalışanlar',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Tarih')),
                ('worked_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Çalışılan Saat')),
                ('is_absent', models.BooleanField(default=False, verbose_name='Devamsızlık')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notlar')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='employee.employee', verbose_name='Çalışan')),
            ],
            options={
                'verbose_name': 'Puantaj',
                'verbose_name_plural': 'Puantajlar',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_type', models.CharField(choices=[('MONTHLY', 'Aylık'), ('HOURLY', 'Saatlik'), ('DAILY', 'Günlük')], max_length=10, verbose_name='Maaş Tipi')),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Temel Maaş')),
                ('extra_hours', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Ek Saatler')),
                ('extra_days', models.IntegerField(default=0, verbose_name='Ek Günler')),
                ('deductions', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Kesintiler')),
                ('working_days_per_month', models.IntegerField(default=22, verbose_name='Aylık Çalışma Günleri')),
                ('working_hours_per_day', models.DecimalField(decimal_places=2, default=8, max_digits=5, verbose_name='Günlük Çalışma Saatleri')),
                ('total_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Toplam Maaş')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Çalışan')),
            ],
            options={
                'verbose_name': 'Maaş',
                'verbose_name_plural': 'Maaşlar',
            },
        ),
    ]