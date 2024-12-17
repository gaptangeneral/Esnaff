from django.urls import path
from . import views
app_name='finance'
urlpatterns = [
    # Kategori işlemleri
    path('kategori/', views.KategoriListView.as_view(), name='kategori_listesi'),
    path('kategori/yeni/', views.KategoriCreateView.as_view(), name='kategori_olustur'),
    path('kategori/<int:pk>/guncelle/', views.KategoriUpdateView.as_view(), name='kategori_guncelle'),
    path('kategori/<int:pk>/sil/', views.KategoriDeleteView.as_view(), name='kategori_sil'),

    # Gelir Gider Takibi
    path('gelir-gider/', views.GelirGiderListView.as_view(), name='gelir_gider_listesi'),
    path('gelir-gider/yeni/', views.GelirGiderCreateView.as_view(), name='gelir_gider_olustur'),
    path('gelir-gider/<int:pk>/guncelle/', views.GelirGiderUpdateView.as_view(), name='gelir_gider_guncelle'),
    path('gelir-gider/<int:pk>/sil/', views.GelirGiderDeleteView.as_view(), name='gelir_gider_sil'),

    # Alacak Verecek Takibi
    path('alacak-verecek/', views.AlacakVerecekListView.as_view(), name='alacak_verecek_listesi'),
    path('alacak-verecek/yeni/', views.AlacakVerecekCreateView.as_view(), name='alacak_verecek_olustur'),
    path('alacak-verecek/<int:pk>/guncelle/', views.AlacakVerecekUpdateView.as_view(), name='alacak_verecek_guncelle'),
    path('alacak-verecek/<int:pk>/sil/', views.AlacakVerecekDeleteView.as_view(), name='alacak_verecek_sil'),

    # Çek Senet Takibi
    path('cek-senet/', views.CekSenetListView.as_view(), name='cek_senet_listesi'),
    path('cek-senet/yeni/', views.CekSenetCreateView.as_view(), name='cek_senet_olustur'),
    path('cek-senet/<int:pk>/guncelle/', views.CekSenetUpdateView.as_view(), name='cek_senet_guncelle'),
    path('cek-senet/<int:pk>/sil/', views.CekSenetDeleteView.as_view(), name='cek_senet_sil'),

    # Fiş İşlemleri
    path('fis/', views.FisListView.as_view(), name='fis_listesi'),
    path('fis/yeni/', views.FisCreateView.as_view(), name='fis_olustur'),
    path('fis/<int:pk>/guncelle/', views.FisUpdateView.as_view(), name='fis_guncelle'),
    path('fis/<int:pk>/sil/', views.FisDeleteView.as_view(), name='fis_sil'),

    # Faturalandırma İşlemleri
    path('fatura/', views.FaturaListView.as_view(), name='fatura_listesi'),
    path('fatura/yeni/', views.FaturaCreateView.as_view(), name='fatura_olustur'),
    path('fatura/<int:pk>/', views.FaturaDetailView.as_view(), name='fatura_detayi'),
    path('fatura/<int:pk>/guncelle/', views.FaturaUpdateView.as_view(), name='fatura_guncelle'),
    path('fatura/<int:pk>/sil/', views.FaturaDeleteView.as_view(), name='fatura_sil'),

    # Veresiye İşlemleri
    path('veresiye/', views.VeresiyeListView.as_view(), name='veresiye_listesi'),
    path('veresiye/yeni/', views.VeresiyeCreateView.as_view(), name='veresiye_olustur'),
    path('veresiye/<int:pk>/guncelle/', views.VeresiyeUpdateView.as_view(), name='veresiye_guncelle'),
    path('veresiye/<int:pk>/sil/', views.VeresiyeDeleteView.as_view(), name='veresiye_sil'),
]