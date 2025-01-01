import sys

def main(input_file, output_file):
    try:
        # Dosyadan yaş değerini oku
        with open(input_file, 'r') as f:
            age = int(f.read().strip())

        # Yaş aralığını belirle
        if age < 15:
            result = "0-14 yaş arası: çocuklar ve ergenler."
        elif age < 65:
            result = "15-64 yaş arası: aktif nüfus veya çalışan nüfus."
        else:
            result = "65 ve üzeri: yaşlı ve bağımlı nüfus."

        # Sonucu çıktı dosyasına yaz
        with open(output_file, 'w') as f:
            f.write(result)

    except Exception as e:
        print(f"Hata: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python age_checker.py <input_file> <output_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
