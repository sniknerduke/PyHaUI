from models import tao_cong_nhan
def nhap_mot_cong_nhan(stt):
    print(f"\nNhập thông tin công nhân thứ {stt}:")
    ma_cn = input("Mã công nhân: ").strip()
    ho_ten = input("Họ tên: ").strip()
    luong_ngay = int(input("Lương ngày: ").strip())
    so_ngay_cong = int(input("Số ngày công: ").strip())
    phu_cap = int(input("Phụ cấp: ").strip())
    return tao_cong_nhan(ma_cn, ho_ten, luong_ngay, so_ngay_cong, phu_cap)
def nhap_danh_sach_cong_nhan():
    n = int(input("Nhập số lượng công nhân: ").strip())
    ds_cong_nhan = []
    for i in range(n):
        cn = nhap_mot_cong_nhan(i + 1)
        ds_cong_nhan.append(cn)
    return ds_cong_nhan
