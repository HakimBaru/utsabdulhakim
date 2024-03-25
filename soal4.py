class BMI_Calculator:
    def __init__(self, berat, tinggi):
        self.berat = berat  # Berat dalam pound
        self.tinggi = tinggi  # Tinggi dalam feet

    def BMI_Value(self):
        return (self.berat / (self.tinggi ** 2)) * 703

    def __eq__(self, other):
        return self.berat == other.berat and self.tinggi == other.tinggi


def main():
    try:
        berat1 = float(input("Masukkan berat orang pertama dalam pound (contoh: 154): "))
        tinggi1 = float(input("Masukkan tinggi orang pertama dalam feet (contoh: 5.7): "))

        berat2 = float(input("Masukkan berat orang kedua dalam pound (contoh: 154): "))
        tinggi2 = float(input("Masukkan tinggi orang kedua dalam feet (contoh: 5.7): "))

        person1 = BMI_Calculator(berat1, tinggi1)
        person2 = BMI_Calculator(berat2, tinggi2)
        if person1 == person2:
            print("Berat dan tinggi kedua orang sama.")
        else:
            print("Berat dan/atau tinggi kedua orang berbeda.")

        print("Nilai BMI untuk orang pertama:", person1.BMI_Value())
        print("Nilai BMI untuk orang kedua:", person2.BMI_Value())

    except ValueError:
        print("Masukkan berat dan tinggi dalam format yang benar.")


if __name__ == "__main__":
    main()