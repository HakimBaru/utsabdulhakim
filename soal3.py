from datetime import datetime, timedelta

tanggal_mulai = datetime.now()
try:
    hari = int(input("Masukkan jumlah hari: "))
    tanggal_akhir = tanggal_mulai + timedelta(days=hari)
    print(f"{tanggal_akhir.strftime('%A')} on {tanggal_akhir.day} {tanggal_akhir.strftime('%B')} {tanggal_akhir.year}")

except ValueError:
    print("Masukkan bilangan bulat.")