jenis_barang = {
    1: "Elektronik",
    2: "Pakaian",
    3: "Makanan/Minuman"
}

barang = {
    "Elektronik": {
        1: "Laptop",
        2: "Handphone",
        3: "Tablet"
    },
    "Pakaian": {
        1: "Kemeja",
        2: "Celana",
        3: "Sweater"
    },
    "Makanan/Minuman": {
        1: "Mie Goreng",
        2: "Soto",
        3: "Es Teh"
    }
}

data_barang = {
    "Laptop": {
        "harga": 5000000,
        "stok": 10
    },
    "Handphone": {
        "harga": 3000000,
        "stok": 20
    },
    "Tablet": {
        "harga": 2000000,
        "stok": 15
    },
    "Kemeja": {
        "harga": 500000,
        "stok": 30
    },
    "Celana": {
        "harga": 400000,
        "stok": 25
    },
    "Sweater": {
        "harga": 300000,
        "stok": 20
    },
    "Mie Goreng": {
        "harga": 15000,
        "stok": 50
    },
    "Soto": {
        "harga": 20000,
        "stok": 40
    },
    "Es Teh": {
        "harga": 10000,
        "stok": 30
    }
}

data_pembelian = {}

print("{:^50}".format('SELAMAT DATANG DI TOKO ONLINE '))
print("{:^50}".format('*'*35))

def proses(pesanan_counter):
    print(f'\nJenis-jenis barang yang tersedia : \n1. Elektronik\n2. Pakaian\n3. Makanan/Minuman')

    plh_jenis = int(input("Pilih Jenis Barang : "))

    if plh_jenis not in jenis_barang:
        print("Jenis barang tidak valid.")
        return False

    print(f"\nBarang yang tersedia untuk jenis {jenis_barang[plh_jenis]} adalah:")
    daftar_barang = barang[jenis_barang[plh_jenis]]
    for nomor, nm_barang in daftar_barang.items():
        print(f"{nomor}. {nm_barang}")

    pilih_barang = int(input("Pilih barang : "))

    if pilih_barang not in daftar_barang:
        print("Barang tidak valid.")
        return False

    barang_terpilih = daftar_barang[pilih_barang]
    data_barang_dipilih = data_barang[barang_terpilih]

    if data_barang_dipilih['stok'] == 0:
        print("Stok barang habis.")
        return False

    print(f"\nNama barang : {barang_terpilih}")
    print(f"Harga barang : {data_barang_dipilih['harga']}")
    print(f"Stok barang : {data_barang_dipilih['stok']}")

    beli = int(input("Jumlah barang yang ingin dibeli : "))

    if beli > data_barang_dipilih['stok']:
        print("Stok barang tidak cukup. Silahkan melakukan pembelian kembali.")
        return False
    
    total = data_barang_dipilih['harga'] * beli
    print(f"\nTotal harga : {total}")

    uang = int(input("Uang pembayaran : "))
    kembalian = uang - total

    if kembalian < 0:
        print("Uang pembayaran tidak cukup. Silahkan melakukan pembelian kembali.")
        return False

    print(f"Kembalian : {kembalian}")

    data_barang_dipilih['stok'] -= beli
    print(f"\nStok barang {barang_terpilih} tersisa : {data_barang_dipilih['stok']}")

    data_pembelian[pesanan_counter] = {
        "nama_barang": barang_terpilih,
        "harga": data_barang_dipilih['harga'],
        "jumlah": beli,
        "total": total,
        "bayar": uang,
        "kembalian": kembalian
    }

    return True

pesanan_counter = 1
while True:
    proses_pembelian = proses(pesanan_counter)

    # Validasi input untuk lanjut belanja
    while True:
        lanjut_input = input("\nLanjut belanja? (y/n) : ").lower()

        if  lanjut_input in ['y', 'yes', 'n', 'no'] :
            break
        else:
            print("Pilihan tidak valid. Silahkan masukkan 'y' atau 'n'.")

    if lanjut_input in ['y', 'yes'] : # Jika lanjut_input = 'y' atau 'yes'
        if proses_pembelian == True:
            pesanan_counter += 1
        continue # Lanjut ke proses belanja selanjutnya
    else:
        print("\nData pembelian :")
        for nomor, detail in data_pembelian.items():
            print(f"\nData pembelian barang ke - {nomor} :")
            print(f"Nama barang : {detail['nama_barang']}")
            print(f"Harga : {detail['harga']}")
            print(f"Jumlah dibeli : {detail['jumlah']}")
            print(f"Total harga : {detail['total']}")
            print(f"Total bayar : {detail['bayar']}")
            print(f"Total kembalian : {detail['kembalian']}")
        exit()