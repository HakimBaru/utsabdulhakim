def calculate_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def main():
    try:
        number = 25
        result = calculate_product(number)
        print("Hasil perkalian dari semua nilai dari 1 hingga 25 adalah:", result)

    except ValueError:
        print("Masukkan bilangan bulat yang valid.")

if __name__ == "__main__":
    main()