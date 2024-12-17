from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Güncellenme Tarihi"))
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_created', on_delete=models.SET_NULL, verbose_name=_("Oluşturan Kullanıcı"))
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_updated', on_delete=models.SET_NULL, verbose_name=_("Güncelleyen Kullanıcı"))

    class Meta:
        abstract = True

class Department(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Departman Adı"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Açıklama"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Departman")
        verbose_name_plural = _("Departmanlar")

class Position(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Pozisyon Adı"))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', verbose_name=_("Departman"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Pozisyon")
        verbose_name_plural = _("Pozisyonlar")

class Employee(BaseModel):
    """
    Çalışan modeli
    """
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Erkek')
        FEMALE = 'FEMALE', _('Kadın')
        OTHER = 'OTHER', _('Diğer')

    class EmployeeType(models.TextChoices):
        FULLTIME = 'FULLTIME', _('Tam Zamanlı')
        PARTTIME = 'PARTTIME', _('Yarı Zamanlı')
        CONTRACT = 'CONTRACT', _('Sözleşmeli')
        INTERN = 'INTERN', _('Stajyer')

    first_name = models.CharField(max_length=100, verbose_name=_("Ad"))
    last_name = models.CharField(max_length=100, verbose_name=_("Soyad"))
    email = models.EmailField(unique=True, verbose_name=_("E-posta"))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("Telefon"))

    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Departman"))
    position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Pozisyon"))

    salary_amount = models.DecimalField(default=1000, max_digits=10, decimal_places=2, verbose_name=_("Maaş"))
    hire_date = models.DateField(verbose_name=_("İşe Başlama Tarihi"))
    is_active = models.BooleanField(default=True, verbose_name=_("Aktif Mi"))
    gender = models.CharField(default='', max_length=10, choices=Gender.choices, verbose_name=_("Cinsiyet"))

    # Yeni eklenen alanlar
    tckn = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name=_("T.C. Kimlik No"))
    sgk_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("SGK No"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Doğum Tarihi"))
    employee_type = models.CharField(max_length=20, choices=EmployeeType.choices, default=EmployeeType.FULLTIME, verbose_name=_("Çalışma Tipi"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        if self.date_of_birth:
            return (datetime.date.today() - self.date_of_birth).days // 365
        return None

    class Meta:
        verbose_name = _("Çalışan")
        verbose_name_plural = _("Çalışanlar")

class Attendance(BaseModel):
    """
    Puantaj modeli
    """
    class EmployeeStatus(models.TextChoices):
        PRESENT = 'PRESENT', _('Geldi')
        ABSENT = 'ABSENT', _('Gelmedi')
        LATE = 'LATE', _('Geç Geldi')
        HALF = 'HALF', _('Yarım Gün')

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="attendance_records",
        verbose_name=_("Çalışan")
    )
    date = models.DateField(verbose_name=_("Tarih"))
    status = models.CharField(max_length=10, choices=EmployeeStatus.choices, default=EmployeeStatus.PRESENT, verbose_name=_("Durum"))
    worked_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name=_("Çalışılan Saat"))
    notes = models.TextField(null=True, blank=True, verbose_name=_("Notlar"))

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date}"

    class Meta:
        verbose_name = _("Puantaj")
        verbose_name_plural = _("Puantajlar")

class Salary(BaseModel):
    """
    Maaş modeli - Brüt/Net ayrımı, ek ödenekler, kesintiler.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_("Çalışan"))
    period_start = models.DateField(null=True, blank=True,verbose_name=_("Dönem Başlangıç"))
    period_end = models.DateField(null=True, blank=True,verbose_name=_("Dönem Bitiş"))
    gross_salary = models.DecimalField(null=True, blank=True,max_digits=10, decimal_places=2, verbose_name=_("Brüt Maaş"))
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Prim/Bonus"))
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Ek Ödenekler"))
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Toplam Kesintiler"))
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Net Maaş"))

    def calculate_net_salary(self):
        # Basit bir örnek hesaplama
        net = self.gross_salary + self.bonuses + self.allowances - self.total_deductions
        return net if net > 0 else 0

    def save(self, *args, **kwargs):
        self.net_salary = self.calculate_net_salary()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Maaş")
        verbose_name_plural = _("Maaşlar")
