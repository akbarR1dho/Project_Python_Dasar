import csv
import pandas as pd
import datetime as dt

TABEL_KAMAR = "tbl_kamar.csv"
TABEL_RESERVASI = "tbl_reservasi.csv"

def buat_reservasi():
    data_kamar = pd.read_csv("tbl_kamar.csv", delimiter=",")
    filter_kamar = data_kamar.query("status == 'tersedia'")

    if filter_kamar.empty:
        print("❗ Tidak ada kamar yang tersedia.")
        return

    print("\n" + "="*60)
    print("🏨  DAFTAR KAMAR YANG TERSEDIA  🏨".center(60))
    print("="*60)
    print(filter_kamar.to_string(index=False))
    print("="*60)

    while True:
        no_kamar = input("🔢 Masukkan no kamar: ").upper()
        if no_kamar in filter_kamar["no_kamar"].values:
            break
        else:
            print("❌ Kamar tidak ditemukan.")
            continue
    
    nm_tamu     = input("👤 Masukkan nama tamu: ")
    jml_hari    = int(input("📅 Masukkan jumlah hari: "))
    total_harga = data_kamar[data_kamar["no_kamar"] == no_kamar]["harga_perhari"].values[0] * jml_hari
    checkin     = dt.datetime.now().strftime("%Y-%m-%d")
    checkout    = (dt.datetime.now() + dt.timedelta(days=jml_hari)).strftime("%Y-%m-%d")
    status      = "checkedin"

    data_reservasi = pd.read_csv(TABEL_RESERVASI, delimiter=",")
    id_reservasi   = 1 if data_reservasi.empty else data_reservasi["id"].max() + 1

    with open(TABEL_RESERVASI, mode="a", newline="") as file_reservasi:
        writer = csv.writer(file_reservasi, delimiter=",")
        writer.writerow([id_reservasi, nm_tamu, no_kamar, total_harga, checkin, checkout, status])

    data_kamar.loc[data_kamar["no_kamar"] == no_kamar, "status"] = "ditempati"
    data_kamar.to_csv(TABEL_KAMAR, index=False, sep=",")
        
    print("✔️ Reservasi berhasil dibuat!")

def checkout_reservasi():
    data_reservasi   = pd.read_csv(TABEL_RESERVASI, delimiter=",")
    filter_reservasi = data_reservasi.query("status == 'checkedin'")

    if filter_reservasi.empty:
        print("❗ Tidak ada tamu yang sedang menginap.")
        return
    
    print("\n📋  DAFTAR TAMU CHECK-IN  📋")
    print(filter_reservasi.to_string(index=False))

    while True:
        id_reservasi = int(input("🔍 Masukkan ID reservasi: "))
        if id_reservasi in filter_reservasi["id"].values:
            break
        else:
            print("❌ Reservasi tidak ditemukan.")
            continue

    data_reservasi.loc[data_reservasi["id"] == id_reservasi, "status"] = "checkedout"
    data_reservasi.to_csv(TABEL_RESERVASI, index=False, sep=",")

    no_kamar   = data_reservasi[data_reservasi["id"] == id_reservasi]["no_kamar"].values[0]
    data_kamar = pd.read_csv(TABEL_KAMAR, delimiter=",")
    data_kamar.loc[data_kamar["no_kamar"] == no_kamar, "status"] = "tersedia"
    data_kamar.to_csv(TABEL_KAMAR, index=False, sep=",")

    print("✔️ Checkout berhasil dilakukan!")

def tampilkan_history():
    data_reservasi = pd.read_csv(TABEL_RESERVASI, delimiter=",")

    if data_reservasi.empty:
        print("⚠️ Belum ada data reservasi.")
        return

    while True:
        print("\n" + "="*40)
        print("📜   RIWAYAT RESERVASI   📜".center(40))
        print("="*40)
        print("1. 📂 Tampilkan semua reservasi")
        print("2. 🛏️  Tamu yang sedang menginap")
        print("3. 🧾  Riwayat checkout")
        print("4. 🔎  Cari berdasarkan ID")
        print("5. ⬅️  Kembali")
        print("-"*40)

        pilih_tampilan = int(input("👉 Pilih tampilan: "))

        if pilih_tampilan == 1:
            print("\n" + "="*78)
            print("📂 SEMUA RESERVASI".center(78))
            print("="*78)
            print(data_reservasi[["id", "nm_tamu", "no_kamar", "total_harga", "status"]].to_string(index=False))
            print("="*78)

        elif pilih_tampilan == 2:
            print("\n" + "="*78)
            print("🛏️  TAMU YANG SEDANG MENGINAP".center(78))
            print("="*78)
            checkedin = data_reservasi.query("status == 'checkedin'")
            if checkedin.empty:
                print("❗ Tidak ada tamu yang sedang menginap.")
            else:
                print(checkedin[["id", "nm_tamu", "no_kamar", "total_harga", "status"]].to_string(index=False))
                print("="*78)

        elif pilih_tampilan == 3:
            print("\n" + "="*73)
            print("🧾  RIWAYAT CHECKOUT".center(78))
            print("="*73)
            checkedout = data_reservasi.query("status == 'checkedout'")
            if checkedout.empty:
                print("❗ Tidak ada riwayat checkout.")
            else:
                print(checkedout[["id", "nm_tamu", "no_kamar", "total_harga", "status"]].to_string(index=False))
                print("="*73)

        elif pilih_tampilan == 4:
            print("\n" + "="*78)
            print("🔎  CARI RESERVASI BERDASARKAN ID".center(78))
            print("="*78)
            while True:
                try:
                    id_reservasi = int(input("➡️ Masukkan ID: "))
                except:
                    print("❌ Harus angka!")
                    continue

                cari = data_reservasi.query("id == @id_reservasi")
                if cari.empty:
                    print("❌ Data tidak ditemukan, coba lagi.")
                else:
                    print("\n✅ Data ditemukan:")
                    print(cari.to_string(index=False))
                    print("="*78)
                    break

        elif pilih_tampilan == 5:
            print("⬅️ Kembali ke menu sebelumnya...")
            break

        else:
            print("❌ Pilihan tidak valid.")

while True:
    print("\n" + "="*37)
    print("🏨  SISTEM RESERVASI HOTEL  🏨".center(34))
    print("="*37)
    print("1. 🛏️ Tampilkan daftar kamar")
    print("2. 📝 Buat reservasi baru")
    print("3. 🚪 Checkout tamu")
    print("4. 📜 Riwayat reservasi")
    print("5. ❌ Keluar")
    print("-"*37)
    
    pilih_aksi = int(input("Pilih aksi: "))

    if pilih_aksi == 1:
        data_kamar = pd.read_csv(TABEL_KAMAR, delimiter=",")
        print("\n" + "="*60)
        print("📋  DAFTAR SELURUH KAMAR  📋".center(60))
        print("="*60)
        if data_kamar.empty:
            print("❗ Data kamar masih kosong")
        else:
            print(data_kamar.to_string(index=False))
        print("="*60)

    elif pilih_aksi == 2:
        buat_reservasi()

    elif pilih_aksi == 3:
        checkout_reservasi()

    elif pilih_aksi == 4:
        tampilkan_history()

    elif pilih_aksi == 5:
        print("👋 Terima kasih telah menggunakan program ini!")
        break
    
    else:
        print("❌ Pilihan tidak valid.")
