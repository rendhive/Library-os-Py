import os

print("Variabel Lingkungan:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

#Menampilkan semua variabel lingkungan yang ada.