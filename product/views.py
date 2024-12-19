from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Supplier, Product, Warehouse, Inventory, StockMovement
from .forms import CategoryForm, SupplierForm, ProductForm, WarehouseForm, InventoryForm, StockMovementForm

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'product/category/category_list.html'  # Düzeltildi
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/category/category_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/category/category_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/category/category_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:category_list')

# Supplier Views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'product/supplier/supplier_list.html'  # Düzeltildi
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/supplier/supplier_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'product/supplier/supplier_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'product/supplier/supplier_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:supplier_list')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'product/product/product_list.html'  # Düzeltildi
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product/product_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product/product_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product/product_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:product_list')

# Warehouse Views
class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'product/warehouse/warehouse_list.html'  # Düzeltildi
    context_object_name = 'warehouses'

class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'product/warehouse/warehouse_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:warehouse_list')

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'product/warehouse/warehouse_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:warehouse_list')

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = 'product/warehouse/warehouse_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:warehouse_list')

# Inventory Views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'product/inventory/inventory_list.html'  # Düzeltildi
    context_object_name = 'inventories'

class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'product/inventory/inventory_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:inventory_list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'product/inventory/inventory_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:inventory_list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'product/inventory/inventory_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:inventory_list')

# Stock Movement Views
class StockMovementListView(ListView):
    model = StockMovement
    template_name = 'product/stock_movement/stock_movement_list.html'  # Düzeltildi
    context_object_name = 'stock_movements'

class StockMovementCreateView(CreateView):
    model = StockMovement
    form_class = StockMovementForm
    template_name = 'product/stock_movement/stock_movement_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:stock_movement_list')

class StockMovementUpdateView(UpdateView):
    model = StockMovement
    form_class = StockMovementForm
    template_name = 'product/stock_movement/stock_movement_form.html'  # Düzeltildi
    success_url = reverse_lazy('product:stock_movement_list')

class StockMovementDeleteView(DeleteView):
    model = StockMovement
    template_name = 'product/stock_movement/stock_movement_confirm_delete.html'  # Düzeltildi
    success_url = reverse_lazy('product:stock_movement_list')