import os

# Daftar folder yang ingin dibuat
folders = [
    'app',
    'app/api',
    'app/services',
    'app/static/css',
    'app/static/js',
    'app/templates',
    'hasil/hasil_dataset_baru',
    'uploads'
]

files = {
    'app/__init__.py': '',
    'app/main.py': '# Entry point FastAPI',
    'app/api/__init__.py': '',
    'app/api/endpoints.py': '# Route API',
    'app/services/__init__.py': '',
    'app/services/ai_service.py': '# Logika AI Load Model',
    'app/templates/base.html': '',
    'app/templates/index.html': '',
    'requirements.txt': 'fastapi\nuvicorn\njinja2\npython-multipart\ntensorflow\nnumpy\npillow',
    '.env': 'MODEL_PATH=hasil/hasil_dataset_baru/CNN_Dataset_Alphabet_Nomor2.keras'
}

def create_structure():
    # Buat Folder
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✔ Folder created: {folder}")

    # Buat File
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"✔ File created: {file_path}")
        else:
            print(f"⚠ File already exists: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\nStruktur folder DisaBicara berhasil dibuat secara otomatis!")