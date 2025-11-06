import os
import shutil

os.makedirs('folder_hapus_folder', exist_ok=True)
shutil.rmtree('folder_hapus_folder')
print("Direktori 'folder_hapus_folder' dan semua isinya telah dihapus.")

#Fungsi: Menghapus direktori dan seluruh isinya secara rekursif.
#Kondisi: Saat Anda ingin menghapus direktori yang memiliki banyak file dan sub-direktori di dalamnya.