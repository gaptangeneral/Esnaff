import os

def get_tree(startpath, prefix=''):
    tree_lines = []
    try:
        # Dizindeki tüm dosya ve klasörleri listele
        files = os.listdir(startpath)
    except PermissionError:
        # İzin hatası alınan dizinlerde atla
        return tree_lines
    files = sorted(files)
    for index, f in enumerate(files):
        path = os.path.join(startpath, f)
        if index == len(files) - 1:
            connector = '└── '
            extension = '    '
        else:
            connector = '├── '
            extension = '│   '
        tree_lines.append(prefix + connector + f)
        if os.path.isdir(path):
            # Alt dizinler için rekürsif olarak çağır
            tree_lines.extend(get_tree(path, prefix + extension))
    return tree_lines

def save_tree_to_file(start_directory, output_file):
    tree = get_tree(start_directory)
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in tree:
            f.write(line + '\n')
    print(f"Dizin yapısı '{output_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    # Başlangıç dizinini belirtin. Örneğin, mevcut dizin:
    start_directory = '.'  # Proje dizininizin yolunu buraya yazabilirsiniz

    # Çıktı dosyasının adı
    output_filename = 'tree_structure.txt'

    # Çıktı dosyasının tam yolunu belirleyin
    output_file_path = os.path.join(start_directory, output_filename)

    save_tree_to_file(start_directory, output_file_path)
