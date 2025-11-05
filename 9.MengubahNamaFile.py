import os

# Membuat file untuk diubah namanya
with open('file_lama.txt', 'w') as f:
    f.write("Ini adalah file lama.")

# Mengubah nama file
if os.path.exists('file_lama.txt'):
    os.rename('file_lama.txt', 'file_baru.txt')
    print("File 'file_lama.txt' telah diganti namanya menjadi 'file_baru.txt'.")
else:
    print("File 'file_lama.txt' tidak ditemukan.")


#Membuat file bernama file_lama.txt dan mengubah namanya menjadi file_baru.txt.