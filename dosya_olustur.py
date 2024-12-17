import os

# Proje kök dizini (manage.py'nin bulunduğu yer)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Finance uygulamasının yolu (varsayalım ki finance uygulamanızın adı bu)
FINANCE_APP_DIR = os.path.join(BASE_DIR, 'finance')

# Finance uygulamasının içindeki templates/finance klasörünün yolu
TEMPLATES_DIR = os.path.join(FINANCE_APP_DIR, 'templates', 'finance')

# Oluşturulacak klasörler ve dosyalar
folders_and_files = {
    'kategori': ['kategori_list.html', 'kategori_form.html', 'kategori_confirm_delete.html'],
    'gelir_gider': ['gelir_gider_list.html', 'gelir_gider_form.html', 'gelir_gider_confirm_delete.html'],
    'alacak_verecek': ['alacak_verecek_list.html', 'alacak_verecek_form.html', 'alacak_verecek_confirm_delete.html'],
    'cek_senet': ['cek_senet_list.html', 'cek_senet_form.html', 'cek_senet_confirm_delete.html'],
    'fis': ['fis_list.html', 'fis_form.html', 'fis_confirm_delete.html'],
    'fatura': ['fatura_list.html', 'fatura_form.html', 'fatura_detail.html', 'fatura_confirm_delete.html'],
    'veresiye': ['veresiye_list.html', 'veresiye_form.html']
}

def create_structure():
    for folder, files in folders_and_files.items():
        folder_path = os.path.join(TEMPLATES_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                pass  # Boş bir dosya oluşturur.

if __name__ == "__main__":
    create_structure()
    print("Finance uygulaması için şablon yapısı oluşturuldu.")