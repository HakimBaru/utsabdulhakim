import datetime


number = int(input("Masukkan bilangan bulat: "))

num_days_this_year = (datetime.date(datetime.date.today().year + 1, 1, 1) - datetime.date(datetime.date.today().year, 1, 1)).days

result = number / num_days_this_year

result_formatted = "{:.11f}".format(result)

print("Hasil pembagian:", result_formatted)