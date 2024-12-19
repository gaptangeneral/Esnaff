from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Category URLs
    path('kategori/', views.CategoryListView.as_view(), name='category_list'),
    path('kategori/yeni/', views.CategoryCreateView.as_view(), name='category_create'),
    path('kategori/<int:pk>/guncelle/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('kategori/<int:pk>/sil/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Supplier URLs
    path('tedarikci/', views.SupplierListView.as_view(), name='supplier_list'),
    path('tedarikci/yeni/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('tedarikci/<int:pk>/guncelle/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('tedarikci/<int:pk>/sil/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    # Product URLs
    path('urun/', views.ProductListView.as_view(), name='product_list'),
    path('urun/yeni/', views.ProductCreateView.as_view(), name='product_create'),
    path('urun/<int:pk>/guncelle/', views.ProductUpdateView.as_view(), name='product_update'),
    path('urun/<int:pk>/sil/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Warehouse URLs
    path('depo/', views.WarehouseListView.as_view(), name='warehouse_list'),
    path('depo/yeni/', views.WarehouseCreateView.as_view(), name='warehouse_create'),
    path('depo/<int:pk>/guncelle/', views.WarehouseUpdateView.as_view(), name='warehouse_update'),
    path('depo/<int:pk>/sil/', views.WarehouseDeleteView.as_view(), name='warehouse_delete'),

    # Inventory URLs
    path('stok/', views.InventoryListView.as_view(), name='inventory_list'),
    path('stok/yeni/', views.InventoryCreateView.as_view(), name='inventory_create'),
    path('stok/<int:pk>/guncelle/', views.InventoryUpdateView.as_view(), name='inventory_update'),
    path('stok/<int:pk>/sil/', views.InventoryDeleteView.as_view(), name='inventory_delete'),

    # Stock Movement URLs
    path('stok-hareketleri/', views.StockMovementListView.as_view(), name='stock_movement_list'),
    path('stok-hareketleri/yeni/', views.StockMovementCreateView.as_view(), name='stock_movement_create'),
    path('stok-hareketleri/<int:pk>/guncelle/', views.StockMovementUpdateView.as_view(), name='stock_movement_update'),
    path('stok-hareketleri/<int:pk>/sil/', views.StockMovementDeleteView.as_view(), name='stock_movement_delete'),
]