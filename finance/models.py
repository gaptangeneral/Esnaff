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
    kasa = models.ForeignKey('Kasa', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kasa")

    def save(self, *args, **kwargs):
        if self.pk is None:  # Yeni bir kayıt ise
            if self.kasa: # Kasa seçiliyse KasaHareketi oluştur
                kasa_hareketi = KasaHareketi(
                    kasa=self.kasa,
                    tutar=self.tutar,
                    açıklama=self.açıklama,
                    tür=self.tür
                )
                kasa_hareketi.save()

                # Kasa bakiyesini güncelleyin
                if self.tür == 'GELİR':
                    self.kasa.bakiye += self.tutar
                else:
                    self.kasa.bakiye -= self.tutar
                self.kasa.save()
            else: # Kasa seçilmediyse hata mesajı göster
                raise ValueError("Lütfen bir kasa seçin.") 

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tür} - {self.tutar} - {self.kategori.ad if self.kategori else 'Kategorisiz'}"

class Fis(models.Model):
    tür = models.CharField(max_length=10, choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')])
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField()
    açıklama = models.TextField(blank=True, null=True)
    kasa = models.ForeignKey('Kasa', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kasa") # Kasa ilişkisi eklendi

    def save(self, *args, **kwargs):
        if self.pk is None:  # Yeni bir kayıt ise
            kasa_hareketi = KasaHareketi(
                kasa=self.kasa,
                tutar=self.tutar,
                açıklama=self.açıklama,
                tür=self.tür
            )
            kasa_hareketi.save()

            # Kasa bakiyesini güncelleyin
            if self.tür == 'GELİR':
                self.kasa.bakiye += self.tutar
            else:
                self.kasa.bakiye -= self.tutar
            self.kasa.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tür} - {self.tutar} - {self.tarih}"

class Fatura(models.Model):
    numara = models.CharField(max_length=50, unique=True)
    müşteri = models.CharField(max_length=255)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField()
    kdv_oranı = models.DecimalField(max_digits=5, decimal_places=2, default=18)
    kasa = models.ForeignKey('Kasa', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kasa") # Kasa ilişkisi eklendi

    def save(self, *args, **kwargs):
        if self.pk is None:  # Yeni bir kayıt ise
            kasa_hareketi = KasaHareketi(
                kasa=self.kasa,
                tutar=self.tutar,
                açıklama=f"Fatura {self.numara}",
                tür='GELİR'  # Fatura gelir olarak kabul ediliyor
            )
            kasa_hareketi.save()

            # Kasa bakiyesini güncelleyin
            self.kasa.bakiye += self.tutar
            self.kasa.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Fatura {self.numara} - {self.müşteri}"

class CekSenet(models.Model):
    tür = models.CharField(max_length=10, choices=[('ÇEK', 'Çek'), ('SENET', 'Senet')])
    numara = models.CharField(max_length=50)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    tarih = models.DateField(verbose_name=("Senet Tarihi"))
    durum = models.BooleanField(default=False)
    kasa = models.ForeignKey('Kasa', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kasa") # Kasa ilişkisi eklendi

    def save(self, *args, **kwargs):
        if self.pk is None:  # Yeni bir kayıt ise
            kasa_hareketi = KasaHareketi(
                kasa=self.kasa,
                tutar=self.tutar,
                açıklama=f"{self.tür} - {self.numara}",
                tür='GELİR' if self.tür == 'ÇEK' else 'GİDER'  # Çek gelir, senet gider olarak kabul ediliyor
            )
            kasa_hareketi.save()

            # Kasa bakiyesini güncelleyin
            if self.tür == 'ÇEK':
                self.kasa.bakiye += self.tutar
            else:
                self.kasa.bakiye -= self.tutar
            self.kasa.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tür} - {self.numara} - {self.tutar}-{self.tarih}"

# Kasa Modeli
class Kasa(models.Model):
    ad = models.CharField(max_length=100, verbose_name="Kasa Adı")
    bakiye = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Bakiye")

    def __str__(self):
        return self.ad

# Kasa Hareketleri Modeli
class KasaHareketi(models.Model):
    kasa = models.ForeignKey(Kasa, on_delete=models.CASCADE, verbose_name="Kasa")
    işlem_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="İşlem Tarihi")
    tutar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tutar")
    açıklama = models.CharField(max_length=255, blank=True, verbose_name="Açıklama")
    tür = models.CharField(max_length=10, choices=[('GELİR', 'Gelir'), ('GİDER', 'Gider')], verbose_name="Tür")

    def __str__(self):
        return f"{self.kasa} - {self.işlem_tarihi} - {self.tutar}"
    
