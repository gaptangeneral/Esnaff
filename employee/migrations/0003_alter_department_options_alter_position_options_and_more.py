# Generated by Django 5.1.3 on 2024-12-15 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_department_remove_employee_department_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Departman', 'verbose_name_plural': 'Departmanlar'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Pozisyon', 'verbose_name_plural': 'Pozisyonlar'},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='is_absent',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='base_salary',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='deductions',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='extra_days',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='extra_hours',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='salary_type',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='total_salary',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='working_days_per_month',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='working_hours_per_day',
        ),
        migrations.AddField(
            model_name='attendance',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('PRESENT', 'Geldi'), ('ABSENT', 'Gelmedi'), ('LATE', 'Geç Geldi'), ('HALF', 'Yarım Gün')], default='PRESENT', max_length=10, verbose_name='Durum'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Güncelleyen Kullanıcı'),
        ),
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama'),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Güncelleyen Kullanıcı'),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.department', verbose_name='Departman'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.position', verbose_name='Pozisyon'),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Güncelleyen Kullanıcı'),
        ),
        migrations.AddField(
            model_name='position',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='position',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='position',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Güncelleyen Kullanıcı'),
        ),
        migrations.AddField(
            model_name='salary',
            name='allowances',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ek Ödenekler'),
        ),
        migrations.AddField(
            model_name='salary',
            name='bonuses',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Prim/Bonus'),
        ),
        migrations.AddField(
            model_name='salary',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AddField(
            model_name='salary',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='salary',
            name='gross_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Brüt Maaş'),
        ),
        migrations.AddField(
            model_name='salary',
            name='net_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Net Maaş'),
        ),
        migrations.AddField(
            model_name='salary',
            name='period_end',
            field=models.DateField(blank=True, null=True, verbose_name='Dönem Bitiş'),
        ),
        migrations.AddField(
            model_name='salary',
            name='period_start',
            field=models.DateField(blank=True, null=True, verbose_name='Dönem Başlangıç'),
        ),
        migrations.AddField(
            model_name='salary',
            name='total_deductions',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Toplam Kesintiler'),
        ),
        migrations.AddField(
            model_name='salary',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AddField(
            model_name='salary',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Güncelleyen Kullanıcı'),
        ),
    ]
