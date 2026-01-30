def tao_cong_nhan(ma_cn, ho_ten, luong_ngay, so_ngay_cong, phu_cap):
    luong_co_ban = luong_ngay * so_ngay_cong
    tong_thu_nhap = luong_co_ban + phu_cap
    return [ma_cn, ho_ten, luong_ngay, so_ngay_cong, phu_cap, luong_co_ban, tong_thu_nhap]
