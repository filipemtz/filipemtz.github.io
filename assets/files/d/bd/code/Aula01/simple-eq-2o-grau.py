
def delta(a, b, c):
    return b ** 2 - 4 * a * c


def raizes(a, b, d):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


def main():
    a = float(input("Coeficiente a:"))
    b = float(input("Coeficiente b:"))
    c = float(input("Coeficiente c:"))

    d = delta(a, b, c)

    if d >= 0:
        x1, x2 = raizes(a, b, d)
        print(f"Raizes: {x1} e {x2}")
    else:
        print("Nao existem raizes reais.")


if __name__ == "__main__":
    main()

