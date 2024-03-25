def main():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
            total = 0
            for line in lines:
                number = int(line.strip())
                total += number
            print("{:,}".format(total))

    except FileNotFoundError:
        print("File 'input.txt' tidak ditemukan.")
    except ValueError:
        print("File 'input.txt' berisi nilai yang tidak valid.")

if __name__ == "__main__":
    main()

