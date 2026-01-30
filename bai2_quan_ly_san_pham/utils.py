def kiem_tra_va_cap_nhat_sp(san_pham, ma_sp, so_luong_moi=100):
    if ma_sp in san_pham:
        print(f"\nSan pham {ma_sp} da co. Cap nhat so luong thanh {so_luong_moi}.")
        san_pham[ma_sp] = so_luong_moi
    else:
        print(f"\nSan pham {ma_sp} chua co. Nhap moi.")
        sl_moi = int(input(f"Nhap so luong cho {ma_sp}: "))
        san_pham[ma_sp] = sl_moi
    return san_pham

def xoa_sp_so_luong_0(san_pham):
    keys_to_remove = [ma_sp for ma_sp, sl in san_pham.items() if sl == 0]
    for k in keys_to_remove:
        del san_pham[k]
    return san_pham

def chuyen_dict_sang_list(san_pham):
    list_ma_sp = list(san_pham.keys())
    list_so_luong = list(san_pham.values())
    return list_ma_sp, list_so_luong

def lay_n_phan_tu_dau(lst, n=3):
    return lst[:n]

def lay_n_phan_tu_cuoi(lst, n=3):
    return lst[-n:]
