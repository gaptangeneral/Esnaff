from django import forms
from .models import Category, Supplier, Product, Warehouse, Inventory, StockMovement
from common.base_forms import BaseForm


class CategoryForm(BaseForm):
    """
    Kategori modeli için form.
    """
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select'}),
        }


class SupplierForm(BaseForm):
    """
    Tedarikçi modeli için form.
    """
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class ProductForm(BaseForm):
    """
    Ürün modeli için form.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'sku', 'category', 'supplier', 'unit_price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'supplier': forms.Select(attrs={'class': 'form-select'}),
        }


class WarehouseForm(BaseForm):
    """
    Depo modeli için form.
    """
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'capacity']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class InventoryForm(BaseForm):
    """
    Stok modeli için form.
    """
    class Meta:
        model = Inventory
        fields = ['product', 'warehouse', 'quantity', 'critical_threshold']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'warehouse': forms.Select(attrs={'class': 'form-select'}),
        }


class StockMovementForm(BaseForm):
    """
    Stok Hareketi modeli için form.
    """
    class Meta:
        model = StockMovement
        fields = ['product', 'warehouse', 'quantity', 'movement_type', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'warehouse': forms.Select(attrs={'class': 'form-select'}),
            'movement_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }