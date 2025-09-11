import congthuc


def main():
    print("=== Chương trình tính toán cơ bản ===")

    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))

    print(f"{a} + {b} = {congthuc.add(a, b)}")
    print(f"{a} - {b} = {congthuc.sub(a, b)}")
    print(f"{a} * {b} = {congthuc.multiple(a, b)}")
    print(f"{a} / {b} = {congthuc.divide(a, b)}")

    print("\n=== Tính căn bậc hai ===")
    x = float(input("Nhập số cần lấy căn bậc hai: "))
    print(f"Căn bậc hai của {x} là: {congthuc.can_bac_hai(x)}")


if __name__ == "__main__":
    main()
