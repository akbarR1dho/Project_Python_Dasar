import csv
from datetime import datetime as dt
import pandas as pd

data = []
id = "4"
df = pd.read_csv("data_kamar.csv", delimiter=";")

while True:
    pilihan = int(input("Masukkan jumlah kamar yang ingin dipesan : "))

    if pilihan == 1:
        filter = df[df["status"] == "tersedia"]
        print(filter)
        # hasil = filter[["no_kamar", "harga_perhari"]]

    elif pilihan == 2:
        filter = df[df["no_kamar"] == id]
        print(filter)
    
    elif pilihan == 3:
        break

    else:
        print("Jumlah kamar yang ingin dipesan tidak sesuai")

data_baru = [
    int(input("Masukkan no kamar : ")), 
    input("Masukkan status : ").lower(), 
    int(input("Masukkan harga perhari : ")),
]

with open("data_kamar.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(data_baru)
    print("Data berhasil ditambahkan")
