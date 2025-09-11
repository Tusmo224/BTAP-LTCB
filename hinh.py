from scr.Ex7.Ex7 import hinhhoc


def main():
    print("=== Tính chu vi và diện tích ===")

    # Hình chữ nhật
    dai = float(input("Nhập chiều dài hình chữ nhật: "))
    rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    print("Chu vi HCN:", hinhhoc.chu_vi_hcn(dai, rong))
    print("Diện tích HCN:", hinhhoc.dien_tich_hcn(dai, rong))
    print("-------------------------")

    # Hình tam giác
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))

    # Kiểm tra điều kiện tam giác hợp lệ
    if a + b > c and a + c > b and b + c > a:
        print("Chu vi tam giác:", hinhhoc.chu_vi_tg(a, b, c))
        print("Diện tích tam giác:", hinhhoc.dien_tich_tg(a, b, c))
    else:
        print("Ba cạnh không tạo thành một tam giác hợp lệ.")
    print("-------------------------")

    # Hình tròn
    r = float(input("Nhập bán kính hình tròn: "))
    print("Chu vi hình tròn:", hinhhoc.chu_vi_ht(r))
    print("Diện tích hình tròn:", hinhhoc.dien_tich_ht(r))

if __name__ == "__main__":
    main()
