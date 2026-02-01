import datetime

# 1. Lớp Tác Giả (Thành phần của Sách)
class TacGia:
    def __init__(self, ten, quoc_tich):
        self.ten = ten
        self.quoc_tich = quoc_tich

    def __str__(self):
        return f"{self.ten} ({self.quoc_tich})"

# 2. Lớp Sách (Lớp Cha)
class Sach:
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.nam_xuat_ban = nam_xuat_ban
        self.tac_gia = tac_gia  # <--- Hợp thành: Chứa đối tượng TacGia

    def get_tuoi_sach(self):
        # Lấy năm hiện tại tự động hoặc fix cứng 2025 theo đề
        nam_hien_tai = 2025  # Hoặc dùng datetime.datetime.now().year
        return nam_hien_tai - self.nam_xuat_ban

    def __str__(self):
        return f"[{self.ma_sach}] {self.ten_sach} - TG: {self.tac_gia}"

    # Nạp chồng toán tử + để gộp tên 2 cuốn sách
    def __add__(self, other):
        # Kiểm tra nếu đối tượng kia cũng là Sách
        if isinstance(other, Sach):
            return f"Tổng hợp: {self.ten_sach} & {other.ten_sach}"
        return "Lỗi: Chỉ cộng được 2 cuốn sách với nhau."

# 3. Các Lớp Kế Thừa
class GiaoTrinh(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, mon_hoc):
        # Gọi lớp cha khởi tạo các thuộc tính chung
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.mon_hoc = mon_hoc

    def __str__(self):
        # Kế thừa in của cha và thêm thông tin môn học
        return f"{super().__str__()} | Môn: {self.mon_hoc} (Giáo trình)"

class ThamKhao(Sach):
    def __init__(self, ma_sach, ten_sach, nam_xuat_ban, tac_gia, linh_vuc):
        super().__init__(ma_sach, ten_sach, nam_xuat_ban, tac_gia)
        self.linh_vuc = linh_vuc

    def __str__(self):
        return f"{super().__str__()} | Lĩnh vực: {self.linh_vuc} (Tham khảo)"

# --- HÀM NHẬP TỪ BÀN PHÍM ---
def nhap_tac_gia():
    print("\n--- Nhập thông tin Tác giả ---")
    ten = input("Tên tác giả: ")
    qt = input("Quốc tịch: ")
    return TacGia(ten, qt)

def nhap_giao_trinh(tac_gia):
    print("\n--- Nhập thông tin Giáo trình ---")
    ma = input("Mã sách: ")
    ten = input("Tên sách: ")
    nam = int(input("Năm xuất bản: "))
    mon = input("Môn học: ")
    return GiaoTrinh(ma, ten, nam, tac_gia, mon)

def nhap_tham_khao(tac_gia):
    print("\n--- Nhập thông tin Sách tham khảo ---")
    ma = input("Mã sách: ")
    ten = input("Tên sách: ")
    nam = int(input("Năm xuất bản: "))
    lv = input("Lĩnh vực: ")
    return ThamKhao(ma, ten, nam, tac_gia, lv)

# --- HÀM IN BẢNG ---
def in_dong_ke_tg():
    print("+" + "-"*25 + "+" + "-"*15 + "+")

def in_bang_tac_gia(ds_tg):
    print("\n" + "="*44)
    print(f"{'DANH SÁCH TÁC GIẢ':^44}")
    in_dong_ke_tg()
    print(f"|{'Tên tác giả':^25}|{'Quốc tịch':^15}|")
    in_dong_ke_tg()
    for tg in ds_tg:
        print(f"|{tg.ten:^25}|{tg.quoc_tich:^15}|")
    in_dong_ke_tg()

def in_dong_ke_sach():
    print("+" + "-"*8 + "+" + "-"*22 + "+" + "-"*6 + "+" + "-"*20 + "+" + "-"*20 + "+" + "-"*12 + "+")

def in_bang_sach(ds_sach):
    print("\n" + "="*94)
    print(f"{'THÔNG TIN TOÀN BỘ SÁCH':^94}")
    in_dong_ke_sach()
    print(f"|{'Mã':^8}|{'Tên sách':^22}|{'Năm':^6}|{'Tác giả':^20}|{'Môn/Lĩnh vực':^20}|{'Tuổi sách':^12}|")
    in_dong_ke_sach()
    
    for s in ds_sach:
        # Lấy thông tin môn học hoặc lĩnh vực
        if isinstance(s, GiaoTrinh):
            mon_lv = s.mon_hoc
            loai = "(Giáo trình)"
        else:
            mon_lv = s.linh_vuc
            loai = "(Tham khảo)"
        
        tuoi = f"{s.get_tuoi_sach()} năm"
        print(f"|{s.ma_sach:^8}|{s.ten_sach:^22}|{s.nam_xuat_ban:^6}|{s.tac_gia.ten:^20}|{mon_lv:^20}|{tuoi:^12}|")
    
    in_dong_ke_sach()

def in_chi_tiet_sach(sach):
    dong_ke = "+" + "-"*20 + "+" + "-"*35 + "+"
    
    print("\n" + dong_ke)
    print(f"|{'Mã sách':^20}|{sach.ma_sach:^35}|")
    print(f"|{'Tên sách':^20}|{sach.ten_sach:^35}|")
    print(f"|{'Năm xuất bản':^20}|{sach.nam_xuat_ban:^35}|")
    print(f"|{'Tác giả':^20}|{sach.tac_gia.ten:^35}|")
    print(f"|{'Quốc tịch TG':^20}|{sach.tac_gia.quoc_tich:^35}|")
    
    if isinstance(sach, GiaoTrinh):
        print(f"|{'Loại sách':^20}|{'Giáo trình':^35}|")
        print(f"|{'Môn học':^20}|{sach.mon_hoc:^35}|")
    elif isinstance(sach, ThamKhao):
        print(f"|{'Loại sách':^20}|{'Tham khảo':^35}|")
        print(f"|{'Lĩnh vực':^20}|{sach.linh_vuc:^35}|")
    
    print(f"|{'Tuổi sách':^20}|{str(sach.get_tuoi_sach()) + ' năm':^35}|")
    print(dong_ke)

def in_ket_qua_cong(chuoi_ket_qua):
    dong_ke = "+" + "-"*60 + "+"
    print("\n" + "="*62)
    print(f"{'KẾT QUẢ PHÉP CỘNG HAI CUỐN SÁCH':^62}")
    print(dong_ke)
    print(f"|{chuoi_ket_qua:^60}|")
    print(dong_ke)

# --- 5. CHƯƠNG TRÌNH CHÍNH ---
def main():
    # Tạo các Tác giả trước (để truyền vào Sách)
    tg1 = TacGia("Quách Tuấn Ngọc", "Việt Nam")
    tg2 = TacGia("Robert Martin", "Mỹ")

    # In danh sách tác giả
    in_bang_tac_gia([tg1, tg2])

    # Tạo danh sách gồm 1 Giáo trình và 1 Tham khảo
    # Lưu ý: Truyền đối tượng tg1, tg2 vào vị trí tham số tac_gia
    gt = GiaoTrinh("GT01", "Ngôn ngữ Pascal", 2000, tg1, "Tin học cơ sở")
    tk = ThamKhao("TK01", "Clean Code", 2008, tg2, "Công nghệ phần mềm")

    ds_sach = [gt, tk]

    # In bảng tổng hợp sách
    in_bang_sach(ds_sach)

    # In chi tiết từng cuốn sách
    print("\n" + "="*60)
    print(f"{'CHI TIẾT TỪNG CUỐN SÁCH':^60}")
    for s in ds_sach:
        in_chi_tiet_sach(s)

    # Thực hiện phép cộng giữa đối tượng Giáo trình và Tham khảo
    chuoi_tong_hop = gt + tk
    in_ket_qua_cong(chuoi_tong_hop)

# --- CHƯƠNG TRÌNH CHÍNH ---
def main_nhap_tu_ban_phim():
    """Hàm nhập từ bàn phím"""
    ds_sach = []
    
    # Nhập số lượng sách
    n = int(input("Nhập số lượng sách: "))
    for i in range(n):
        print(f"\n=== Sách thứ {i+1} ===")
        tg = nhap_tac_gia()
        
        loai = input("Loại sách (1: Giáo trình, 2: Tham khảo): ")
        if loai == "1":
            ds_sach.append(nhap_giao_trinh(tg))
        else:
            ds_sach.append(nhap_tham_khao(tg))
    
    # In bảng
    in_bang_sach(ds_sach)
    
    # Phép cộng 2 sách đầu tiên nếu có
    if len(ds_sach) >= 2:
        chuoi = ds_sach[0] + ds_sach[1]
        in_ket_qua_cong(chuoi)

def main():
    """Hàm chạy với dữ liệu mẫu"""
    # Tạo tác giả mẫu
    tg1 = TacGia("Quách Tuấn Ngọc", "Việt Nam")
    tg2 = TacGia("Robert Martin", "Mỹ")

    in_bang_tac_gia([tg1, tg2])

    # Tạo sách mẫu
    gt = GiaoTrinh("GT01", "Ngôn ngữ Pascal", 2000, tg1, "Tin học cơ sở")
    tk = ThamKhao("TK01", "Clean Code", 2008, tg2, "Công nghệ phần mềm")

    ds_sach = [gt, tk]

    in_bang_sach(ds_sach)

    # In chi tiết
    print("\n" + "="*60)
    print(f"{'CHI TIẾT TỪNG CUỐN SÁCH':^60}")
    for s in ds_sach:
        in_chi_tiet_sach(s)

    # Phép cộng
    chuoi_tong_hop = gt + tk
    in_ket_qua_cong(chuoi_tong_hop)

if __name__ == "__main__":
    main()  # Chạy với dữ liệu mẫu
    # main_nhap_tu_ban_phim()  # Bỏ comment để nhập từ bàn phím
