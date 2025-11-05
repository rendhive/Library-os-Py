import os

# Membuat file contoh untuk dihapus
with open('file_sample.txt', 'w') as f:
    f.write("Ini adalah file contoh.")

# Menghapus file
if os.path.exists('file_sample.txt'):
    os.remove('file_sample.txt')
    print("File 'file_sample.txt' telah dihapus.")
else:
    print("File 'file_sample.txt' tidak ditemukan.")


#Membuat file contoh dan kemudian menghapusnya setelah memastikan file tersebut ada.