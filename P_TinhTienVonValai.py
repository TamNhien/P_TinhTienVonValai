def main():
    T = float(input("Nhập số tiền gửi ban đầu (triệu đồng) : "))
    print("Năm\tTiền vốn (triệu)\tLãi (triệu)")

    for nam in range(1, 16):
        tien_von = T * (1 + 0.08) ** nam
        tien_lai = T * 0.08 * nam
        print(f"{nam}\t{tien_von:.2f}\t\t\t{tien_lai:.2f}")

if __name__ == "__main__":
    main()

