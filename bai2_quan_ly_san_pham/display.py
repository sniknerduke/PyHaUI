def in_dong_ke_loai():
    print("+" + "-"*12 + "+" + "-"*25 + "+")

def in_dong_ke_sp():
    print("+" + "-"*12 + "+" + "-"*15 + "+")

def in_bang_loai_san_pham(loai_san_pham):
    print("\nDANH MUC LOAI SAN PHAM:")
    in_dong_ke_loai()
    print(f"|{'Ma Loai':^12}|{'Ten Loai':^25}|")
    in_dong_ke_loai()
    for ma, ten in loai_san_pham.items():
        print(f"|{ma:^12}|{ten:^25}|")
    in_dong_ke_loai()

def in_bang_san_pham(san_pham, tieu_de="DANH SACH SAN PHAM"):
    print(f"\n{tieu_de}:")
    in_dong_ke_sp()
    print(f"|{'Ma SP':^12}|{'So Luong':^15}|")
    in_dong_ke_sp()
    for ma, sl in san_pham.items():
        print(f"|{ma:^12}|{sl:>14,} |")
    in_dong_ke_sp()
