# =================================== praktikum 1 ===================================
# import os 
# # Fungsi untuk mengecek dan membuat folder 
# def buat_folder(nama_folder): 
#     if not os.path.exists(nama_folder): 
#         os.mkdir(nama_folder) 
#         print(f"Folder '{nama_folder}' berhasil dibuat.") 
#     else: 
#         print(f"Folder '{nama_folder}' sudah ada.")
        
# def simpan_data(nama_file, isi_teks): 
#     # 'a' berarti append (menambah tanpa menghapus isi lama) 
#     with open(nama_file, 'a') as f: 
#         f.write(isi_teks + "\n") 
#     print(f"Data berhasil disimpan ke {nama_file}") 
 
# # Memanggil fungsi 
# buat_folder("Data_Scraping") 

# =================================== tugas 1 ===================================

import os

# Fungsi membuat folder
def buat_folder(nama_folder):
    if not os.path.exists(nama_folder):
        os.mkdir(nama_folder)
        print(f"{nama_folder} : False -> Folder belum ada, sekarang berhasil dibuat")
    else:
        print(f"{nama_folder} : True -> Folder sudah tersedia")

# Fungsi membuat file
def buat_file(path_file, isi_text):
    if not os.path.exists(path_file):
        with open(path_file, "w") as file:
            file.write(isi_text)
        print(f"{path_file} : False -> File belum ada, sekarang berhasil dibuat")
    else:
        print(f"{path_file} : True -> File sudah tersedia")

# Membuat 5 folder
for i in range(1, 6):
    nama_folder = f"Kategori_{i}"

    # Membuat folder
    buat_folder(nama_folder)

    # Membuat 5 file di dalam setiap folder
    for j in range(1, 6):
        nama_file = f"{nama_folder}/file_{j}.txt"
        isi = f"Ini adalah isi dari file {j} pada {nama_folder}"

        buat_file(nama_file, isi)