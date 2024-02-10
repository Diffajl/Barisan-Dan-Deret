def barisan_aritmatika(a, n, b):
    print("Un = a + (n - 1) x b")
    print(f"Un = {a} + ({n} - 1) x {b}")
    print("Un = {} + ({}) x {}".format(a,n - 1, b))
    print("Un = {} + {}".format(a, (n - 1) * b))
    print("Un = {}".format(a + (n-1) * b))

def deret_aritmatika():
    menu_deret_aritmatika()
    choice_rumus = input("Pilih Rumus Diatas : ")
    if choice_rumus in ["1", "Sn = n/2(2a+(n-1)x b"]:
        print("Deret Aritmatika Rumus Kesatu")
        n = int(input("Masukan Suku Ke-n : "))
        a = int(input("Masukan Suku Pertama : "))
        b = int(input("Masukan Beda(U2 - U1) : "))
        print("Sn = n/2 (2a+(n-1) x b")
        print(f"Sn = {n}/2 (2 x {a} + ({n}-1) x {b})")
        print("Sn = {}/2 ({} + ({}) x {})".format(n, 2 * a,(n - 1),b))
        print("Sn = {}/2 ({} + {})".format(n, 2 * a, (n - 1) * b))
        print("Sn = {}/2 ({})".format(n, 2*a + (n - 1) * b))
        print("Sn = {}".format(n/2 * (2*a+(n-1)*b)))

    elif choice_rumus in ["2", "Sn = n/2(a+un)"]:
        print("Deret Aritmatika Rumus Kedua")
        n = int(input("Masukan Suku Ke-n : "))
        a = int(input("Masukan Suku Pertama : "))
        un = int(input("Masukan Un : "))
        print("Sn = n/2(a+un)")
        print(f"Sn = {n}/2 ({a} + {un})")
        print("Sn = {}/2 ({})".format(n, a + un))
        print("Sn = {}".format(n/2 * (a + un)))

    else:
        return "Pilihan Tidak Valid."
    
def barisan_geometri(a, r, n):
    print("Un = a x r^n")
    print(f"Un = {a} x {r}^{n}")
    print("Un = {} x {}".format(a, r**n))
    print("Un = {}".format(a * (r**n)))

def deret_geometri_naik(a, r, n):
    print("Sn = a (r^n - 1) ")
    print("     -----------")
    print("        r - 1  ")
    print("\t")
    print(f"Sn = {a} ({r}^{n} - 1)")
    print("     -----------")
    print(f"        {r} - 1")
    print("\t")
    print("Sn = {} ({}^{} - 1)".format(a, r, n))
    print("     -----------")
    print("         {}".format(r - 1))
    print("\t")
    print("Sn = {} ({})".format(a, (r**n) - 1))
    print("     -----------")
    print("         {}".format(r - 1))
    print("\t")
    print("Sn = {}".format(a * (r**(n) - 1)))
    print("-----------")
    print("    {}".format(r - 1))
    print("Sn = {}".format(a * (r**(n) - 1) / (r - 1)))
    print("\t")

def deret_geometri_turun(a, r, n):
    print("Sn = a (1 - r^n)")
    print("     -----------")
    print("        1 - r    ")
    print("\t")
    print(f"Sn = {a} (1 - {r}^{n})")
    print("     -----------")
    print(f"        1 - {r}    ")
    print("\t")
    print("Sn = {} (1 - {})".format(a, r**n))
    print("     -----------")
    print("         {}".format(1 - r))
    print("\t")
    print("Sn = {} ({})".format(a, 1 - (r**n)))
    print("     -----------")
    print("         {}".format(1 - r))
    print("\t")
    print("Sn = {}".format(a * (1 - r**n)))
    print("     -----------")
    print("         {}".format(1 - r))
    print("\t")
    print("Sn = {}".format((a * (1 - r**n)) / (1 - r)))

def deret_geometri_tak_hingga(a, r):
    print("S∞ =  a ")
    print("    ----")
    print("    1-r")
    print("\t")
    print(f"S∞ = {a}")
    print("    ----")
    print(f"    1-{r}")
    print("\t")
    print(f"S∞ = {a}")
    print("    ----")
    print("     {}".format(1 - r))
    print("\t")
    print("S∞ = {}".format(a / (1 - r)))

def menu():
    print("\n")
    print("+----------------------------------------+")
    print("|            Barisan Dan Deret           |")
    print("+----------------------------------------+")
    print("|         1. Barisan Aritmatika          |")
    print("|         2. Deret Arimatika             |")
    print("|         3. Barisan Geometri            |")
    print("|         4. Deret Geometri Naik         |")
    print("|         5. Deret Geometri Turun        |")
    print("|         6. Deret Geometri Tak Hingga   |")
    print("+----------------------------------------+")
    print("\t")

def menu_deret_aritmatika():
    print("\t")
    print("+----------------------------+")
    print("|        Pilih Rumus         |")
    print("+----------------------------+")
    print("|    1.Sn = n/2(2a+(n-1)x b) |")
    print("|    2.Sn = n/2(a+un)        |")
    print("+----------------------------+")
    print("\t")

def main():
    while True:
        menu()
        choice = input("Masukan Program Yang Ingin Anda Gunakan : ")
        if choice in ["1", "Barisan Aritmatika", "barisan aritmatika", "Barisan aritmatika", "barisan Aritmatika"]:
            print("Barisan Aritmatika")
            a = int(input("Masukan Suku Pertama : "))
            n = int(input("Masukan Suku Ke-n : "))
            b = int(input("Masukan Beda(U2 - U1) : "))
            result = barisan_aritmatika(a, n, b)

        elif choice in ["2", "Deret Aritmatika", "deret aritmatika", "Deret aritmatika", "deret Aritmatika"]:
            result = deret_aritmatika()
        
        elif choice in ["3", "Barisan Geometri", "barisan geometri", "Barisan geometri", "barisan Geometri"]:
            print("Barisan Geometri")
            a = int(input("Masukan Suku Pertama : "))
            n = int(input("Masukan Suku Ke-n : "))
            r = int(input("Masukan Rasio(U2 / U1) : "))
            result = barisan_geometri(a, n, r)

        elif choice in ["4", "Deret Geometri Naik", "Deret geometri naik", "deret geometri naik"]:
            print("Deret Geometri Naik")
            a = int(input("Masukan Suku Pertama : "))
            r = int(input("Masukan Rasio(U2 / U1) : "))
            n = int(input("Masukan Suku Ke-n : "))
            result = deret_geometri_naik(a, r, n)

        elif choice in ["5", "Deret Geometri Turun", "Deret geometri turun", "deret geometri turun"]:
            print("Deret Geometri Turun")
            a = int(input("Masukan Suku Pertama : "))
            r = float(input("Masukan Rasio(U2 / U1) : "))
            n = int(input("Masukan Suku Ke-n : "))
            result = deret_geometri_turun(a, r, n)

        elif choice in ["6", "Deret Geometri Tak Hingga", "Deret geometri tak hingga", "deret geometri tak terhingga"]:
            a = int(input("Masukan Suku Pertama : "))
            r = float(input("Masukan Rasio(U2 / U1) : "))
            result = deret_geometri_tak_hingga(a, r)

        else:
            print("Pilihan Tidak Valid!")
            break

if __name__ == "__main__":
    main()