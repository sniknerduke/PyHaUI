def nhap_san_pham():
    n = int(input("Nhập số lượng sản phẩm (n): ").strip())
    
    san_pham = {}
    for i in range(n):
        ma_sp = input(f"Nhập mã SP thứ {i+1}: ").strip()
        so_luong = int(input(f"Nhập số lượng tồn kho cho {ma_sp}: ").strip())
        san_pham[ma_sp] = so_luong
    return san_pham

def nhap_loai_san_pham():
    m = int(input("\nNhập số lượng loại sản phẩm (m): ").strip())
    
    loai_san_pham = {}
    for i in range(m):
        ma_loai = input(f"Nhập mã loại SP thứ {i+1}: ").strip()
        ten_loai = input(f"Nhập tên loại SP cho {ma_loai}: ").strip()
        loai_san_pham[ma_loai] = ten_loai
    return loai_san_pham
