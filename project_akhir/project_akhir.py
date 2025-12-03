import csv
import pandas as pd
import datetime as dt

# Program reservasi hotel sederhana

TABEL_KAMAR = "tbl_kamar.csv"
TABEL_RESERVASI = "tbl_reservasi.csv"

# # BACA DATA KAMAR
# def baca_data_kamar():
#     kamar = []
#     with open(TABEL_KAMAR, mode="r") as file_kamar:
#         reader = csv.DictReader(file_kamar)
#         for row in reader:
#             kamar.append(row)
#     return kamar

def buat_reservasi():
    data_kamar = pd.read_csv(TABEL_KAMAR, delimiter=",")
    filter_kamar = data_kamar.query("status == 'tersedia'")
    print()
    print(filter_kamar)

    while True:
        no_kamar = input("Masukkan no kamar: ").upper()
        if no_kamar in filter_kamar["no_kamar"].values:
            break
        else:
            print("Kamar tidak ditemukan.")
            continue
    
    # Membuat reservasi
    nm_tamu = input("Masukkan nama tamu: ")
    jml_hari = int(input("Masukkan jumlah hari: "))
    total_harga = data_kamar[data_kamar["no_kamar"] == no_kamar]["harga_perhari"].values[0] * jml_hari
    checkin = dt.datetime.now().strftime("%Y-%m-%d")
    checkout = (dt.datetime.now() + dt.timedelta(days=jml_hari)).strftime("%Y-%m-%d")
    status = "checkedin"
    data_reservasi = pd.read_csv(TABEL_RESERVASI, delimiter=",")
    if data_reservasi.empty:
        id_reservasi = 1
    else:
        id_reservasi = data_reservasi["id"].max() + 1

    # Simpan reservasi ke file
    with open(TABEL_RESERVASI, mode="a", newline="") as file_reservasi:
        writer = csv.writer(file_reservasi, delimiter=",")
        writer.writerow([id_reservasi, nm_tamu, no_kamar, total_harga, checkin, checkout, status])

    # Ubah status kamar menjadi ditempati
    data_kamar.loc[data_kamar["no_kamar"] == no_kamar, "status"] = "ditempati"
    data_kamar.to_csv(TABEL_KAMAR, index=False, sep=",")
        
    print("Reservasi berhasil dibuat.")

def checkout_reservasi():
    data_reservasi = pd.read_csv(TABEL_RESERVASI, delimiter=",")
    filter_reservasi = data_reservasi.query("status == 'checkedin'")
    print()
    print(filter_reservasi)

    while True:
        id_reservasi = int(input("Masukkan ID reservasi: "))
        if id_reservasi in filter_reservasi["id"].values:
            break
        else:
            print("Reservasi tidak ditemukan.")
            continue

    # Ubah status reservasi menjadi checkout
    data_reservasi.loc[data_reservasi["id"] == id_reservasi, "status"] = "checkedout"
    data_reservasi.to_csv(TABEL_RESERVASI, index=False, sep=",")

    # Ubah status kamar menjadi tersedia
    no_kamar = data_reservasi[data_reservasi["id"] == id_reservasi]["no_kamar"].values[0]
    data_kamar = pd.read_csv(TABEL_KAMAR, delimiter=",")
    data_kamar.loc[data_kamar["no_kamar"] == no_kamar, "status"] = "tersedia"
    data_kamar.to_csv(TABEL_KAMAR, index=False, sep=",")

    print("Checkout berhasil dilakukan.")

def tampilkan_history():
    data_reservasi = pd.read_csv(TABEL_RESERVASI, delimiter=",")
    
    while True:
        print("""
Pilihan tampilan history: 
1. Semua reservasi
2. Reservasi status checkedin
3. Reservasi status checkedout
4. Cari reservasi
5. Kembali""")
        pilih_tampilan = int(input("Pilih tampilan: "))
        if pilih_tampilan == 1:
            print(data_reservasi)

        elif pilih_tampilan == 2:
            filter_reservasi_checkedin = data_reservasi.query("status == 'checkedin'")
            if filter_reservasi_checkedin.empty:
                print("Tidak ada reservasi checkedin.")
            else:
                print(filter_reservasi_checkedin)

        elif pilih_tampilan == 3:
            filter_reservasi_checkout = data_reservasi.query("status == 'checkedout'")
            if filter_reservasi_checkout.empty:
                print("Tidak ada reservasi checkout.")
            else:
                print(filter_reservasi_checkout)

        elif pilih_tampilan == 4:
            while True:
                id_reservasi = int(input("Masukkan id reservasi: "))
                cari_reservasi = data_reservasi.query("id == @id_reservasi")
                if cari_reservasi.empty:
                    print("Reservasi tidak ditemukan.\n")
                else:
                    print(cari_reservasi)
                    break

        elif pilih_tampilan == 5:
            break
        else:
            print("Pilihan tidak valid.")

while True:
    print("""
Pilihan aksi: 
1. Tampilkan data kamar 
2. Buat reservasi 
3. Checkout reservasi 
4. Reservasi history 
5. Keluar""")
    
    pilih_aksi = int(input("Pilih aksi: "))

    if pilih_aksi == 1:
        data_kamar = pd.read_csv("tbl_kamar.csv", delimiter=",")
        if data_kamar.empty:
            print("Data kamar masih kosong\n")
        else:
            print(data_kamar)

    elif pilih_aksi == 2:
        buat_reservasi()

    elif pilih_aksi == 3:
        checkout_reservasi()

    elif pilih_aksi == 4:
        tampilkan_history()

    elif pilih_aksi == 5:
        print("Terimakasih telah menggunakan program ini.")
        break
    
    else:
        print("Pilihan tidak valid.\n")