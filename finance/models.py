from django.db import models


class Kategori(models.Model):
    ad = models.CharField(max_length=100)
    tür = models.CharField(max_length=10, choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')])

    def __str__(self):
        return f"{self.ad} ({self.tür})"

class AlacakVerecek(models.Model):
    kişi = models.CharField(max_length=255)
    tür = models.CharField(max_length=10, choices=[('ALACAK', 'Alacak'), ('BORÇ', 'Borç')])
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    son_odeme_tarihi = models.DateField()
    durum = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.kişi} - {self.tür} - {self.tutar}"

class Veresiye(models.Model):
    kişi = models.CharField(max_length=255)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    son_odeme_tarihi = models.DateField()
    durum = models.BooleanField(default=False)
    alacak_verecek = models.OneToOneField(AlacakVerecek, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.kişi} - {self.tutar} - {'Ödendi' if self.durum else 'Ödenmedi'}"


class GelirGider(models.Model):
    TÜR_SEÇENEKLERİ = [
        ('GELİR', 'Gelir'),
        ('GİDER', 'Gider'),
    ]
    tür = models.CharField(max_length=10, choices=TÜR_SEÇENEKLERİ)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    açıklama = models.TextField(blank=True, null=True)
    tarih = models.DateField(auto_now_add=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tür} - {self.tutar} - {self.kategori.ad if self.kategori else 'Kategorisiz'}"


class Fis(models.Model):
    tür = models.CharField(max_length=10, choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')])
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField()
    açıklama = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tür} - {self.tutar} - {self.tarih}"

class Fatura(models.Model):
    numara = models.CharField(max_length=50, unique=True)
    müşteri = models.CharField(max_length=255)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField()
    kdv_oranı = models.DecimalField(max_digits=5, decimal_places=2, default=18)

    def __str__(self):
        return f"Fatura {self.numara} - {self.müşteri}"

class CekSenet(models.Model):
    tür = models.CharField(max_length=10, choices=[('ÇEK', 'Çek'), ('SENET', 'Senet')])
    numara = models.CharField(max_length=50)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField(verbose_name=("Senet Tarihi"))
    durum = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tür} - {self.numara} - {self.tutar}-{self.tarih}"