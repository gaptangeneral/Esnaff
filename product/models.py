from django.db import models

# Kategoriler için model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Kategori adı (benzersiz)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')  # Üst kategori (hiyerarşik yapı için)

    class Meta:
        verbose_name_plural = "Kategoriler"  # Türkçe çoğul isim

    def __str__(self):
        return self.name  # Kategori adını döndür


# Tedarikçiler için model
class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Tedarikçi adı (benzersiz)
    contact_name = models.CharField(max_length=255, blank=True)  # İletişim kişisi adı
    phone = models.CharField(max_length=20, blank=True)  # Telefon numarası
    address = models.TextField(blank=True)  # Adres

    class Meta:
        verbose_name_plural = "Tedarikçiler"  # Türkçe çoğul isim

    def __str__(self):
        return self.name  # Tedarikçi adını döndür

# Ürünler için model
class Product(models.Model):
    name = models.CharField(max_length=255)  # Ürün adı
    description = models.TextField(blank=True)  # Ürün açıklaması
    sku = models.CharField(max_length=50, unique=True)  # Stok Tutma Birimi (SKU) (benzersiz)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Ürün kategorisi (ilişki)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)  # Ürün tedarikçisi (ilişki)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Birim fiyatı
    image = models.ImageField(upload_to='product_images/', blank=True)  # Ürün resmi
    # Barkod ve QR kod desteği için alanlar daha sonra eklenecek

    class Meta:
        verbose_name_plural = "Ürünler"  # Türkçe çoğul isim

    def __str__(self):
        return f"{self.name} ({self.sku})"  # Ürün adı ve SKU'sunu döndür


# Depolar için model
class Warehouse(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Depo adı (benzersiz)
    address = models.TextField(blank=True)  # Depo adresi
    capacity = models.PositiveIntegerField(null=True, blank=True)  # Depo kapasitesi

    class Meta:
        verbose_name_plural = "Depolar"  # Türkçe çoğul isim

    def __str__(self):
        return self.name  # Depo adını döndür


# Stoklar için model
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Ürün (ilişki)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)  # Depo (ilişki)
    quantity = models.PositiveIntegerField(default=0)  # Stok miktarı
    critical_threshold = models.PositiveIntegerField(default=10)  # Kritik stok eşiği

    class Meta:
        verbose_name_plural = "Stoklar"  # Türkçe çoğul isim
        unique_together = ('product', 'warehouse')  # Bir ürün bir depoda sadece bir kez bulunabilir

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name} ({self.quantity})"  # Ürün, depo ve miktar bilgisini döndür

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Önce kaydet
        self.check_critical_threshold()  # Kritik eşiği kontrol et

    def check_critical_threshold(self):
        if self.quantity <= self.critical_threshold:
            # Kritik stok uyarısı oluştur (örneğin, e-posta veya bildirim gönder)
            # ... (burada uyarı mekanizmasını implemente edeceğiz)
            # Finance modülüne veri gönder (örneğin, düşük stok bildirimi)
            # ... (burada finance modülü ile entegrasyonu sağlayacağız)
            print(f"Kritik stok uyarısı: {self.product.name} - {self.warehouse.name} ({self.quantity})")  # Konsola uyarı mesajı yazdır

class StockMovement(models.Model): # StockMovement sınıfı Product ve Inventory sınıflarından sonra tanımlanmalı
    """
    Stok hareketlerini temsil eden model.
    """
    MOVEMENT_TYPES = (
        ('IN', 'Giriş'),
        ('OUT', 'Çıkış'),
        ('TRANSFER', 'Transfer'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Hareketin ait olduğu ürün
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)  # Hareketin gerçekleştiği depo
    quantity = models.PositiveIntegerField()  # Hareket miktarı
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)  # Hareket türü (giriş, çıkış, transfer)
    date = models.DateTimeField(auto_now_add=True)  # Hareket tarihi (otomatik olarak ayarlanır)
    description = models.TextField(blank=True)  # Hareket açıklaması (isteğe bağlı)

    class Meta:
        verbose_name_plural = "Stok Hareketleri"  # Türkçe çoğul isim

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name} - {self.get_movement_type_display()} ({self.quantity})"  # Stok hareketi bilgisini döndür

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Önce kaydet
        self.update_inventory()  # Stokları güncelle

    def update_inventory(self):
        """
        Stok hareketine göre ilgili envanter kaydını günceller.
        """
        inventory, created = Inventory.objects.get_or_create(product=self.product, warehouse=self.warehouse)  # İlgili envanter kaydını al veya oluştur
        if self.movement_type == 'IN':
            inventory.quantity += self.quantity  # Giriş ise stoğu artır
        elif self.movement_type == 'OUT':
            inventory.quantity -= self.quantity  # Çıkış ise stoğu azalt
        elif self.movement_type == 'TRANSFER':
            # Transfer işlemleri için ilgili depolardaki stokları güncelleyin
            # ... (burada transfer işlemi için stok güncelleme mantığı eklenecek)
            pass  # Şimdilik boş bırak
        inventory.save()  # Envanter kaydını kaydet