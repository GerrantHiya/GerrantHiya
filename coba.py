from datetime import datetime

tanggal_input = input("Masukkan tanggal (YYYY-MM-DD): ")
tanggal_tertentu = input("Masukkan tanggal tertentu (YYYY-MM-DD): ")

#tanggal_input = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
#tanggal_tertentu = datetime.strptime(tanggal_tertentu, "%Y-%m-%d").date()

if tanggal_input < tanggal_tertentu:
    print("kurang")
elif tanggal_input > tanggal_tertentu:
    print("lebih")
else:
    print("sama")
