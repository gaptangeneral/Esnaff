import os

def create_product_templates():
    """
    product/templates/product dizini altında gerekli klasörleri ve HTML dosyalarını oluşturur.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, 'templates', 'product')

    # Oluşturulacak klasörler ve dosyalar
    folders_and_files = {
        'category': [
            'category_list.html', 
            'category_form.html', 
            'category_confirm_delete.html'
        ],
        'supplier': [
            'supplier_list.html', 
            'supplier_form.html', 
            'supplier_confirm_delete.html'
        ],
        'product': [
            'product_list.html', 
            'product_form.html', 
            'product_confirm_delete.html'
        ],
        'warehouse': [
            'warehouse_list.html', 
            'warehouse_form.html', 
            'warehouse_confirm_delete.html'
        ],
        'inventory': [
            'inventory_list.html', 
            'inventory_form.html', 
            'inventory_confirm_delete.html'
        ],
        'stock_movement': [
            'stock_movement_list.html', 
            'stock_movement_form.html', 
            'stock_movement_confirm_delete.html'
        ],
    }

    for folder, files in folders_and_files.items():
        folder_path = os.path.join(template_dir, folder)
        os.makedirs(folder_path, exist_ok=True)  # Klasörü oluşturur, varsa hata vermez
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                # Temel bir şablon yaz
                f.write("{% extends \"product/base_product.html\" %}\n")
                f.write("\n")
                f.write("{% block product_content %}\n")
                f.write("\n")
                f.write("{% endblock %}")

if __name__ == "__main__":
    create_product_templates()
    print("Ürün şablonları oluşturuldu.")