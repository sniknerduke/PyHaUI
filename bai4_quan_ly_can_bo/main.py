from abc import ABC, abstractmethod

# 1. Lớp Trừu tượng (Cha)
class CanBo(ABC):
    def __init__(self, ma_cb, ho_ten, nam_sinh):
        self.ma_cb = ma_cb
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh

    # Phương thức trừu tượng: Chỉ khai báo tên, không viết code
    @abstractmethod
    def tinh_luong(self):
        pass

    def __str__(self):
        return f"[{self.ma_cb}] {self.ho_ten} ({self.nam_sinh})"

# 2. Lớp Công Nhân (Con)
class CongNhan(CanBo):
    def __init__(self, ma_cb, ho_ten, nam_sinh, ngay_cong):
        # Gọi hàm khởi tạo của cha
        super().__init__(ma_cb, ho_ten, nam_sinh)
        self.ngay_cong = ngay_cong

    # Bắt buộc phải viết code cho hàm trừu tượng này
    def tinh_luong(self):
        return self.ngay_cong * 500000

    def __str__(self):
        # Tái sử dụng hàm in của cha và nối thêm thông tin riêng
        return f"Công Nhân: {super().__str__()} | Lương: {self.tinh_luong():,.0f} VNĐ"

# 3. Lớp Kỹ Sư (Con)
class KySu(CanBo):
    def __init__(self, ma_cb, ho_ten, nam_sinh, he_so_luong):
        super().__init__(ma_cb, ho_ten, nam_sinh)
        self.he_so_luong = he_so_luong

    # Cách tính lương khác hẳn Công nhân
    def tinh_luong(self):
        return self.he_so_luong * 2000000

    def __str__(self):
        return f"Kỹ Sư:   {super().__str__()} | Lương: {self.tinh_luong():,.0f} VNĐ"

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    # Tạo danh sách hỗn hợp (Polymorphism - Đa hình)
    # Không cần chia làm 2 danh sách riêng, cứ ném hết vào 1 list
    ds_nhan_vien = [
        CongNhan("CN01", "Nguyen Van A", 1990, 26),      # Làm 26 công
        CongNhan("CN02", "Tran Thi B", 1995, 24),        # Làm 24 công
        KySu("KS01", "Le Van C", 1988, 5.0),             # Hệ số 5.0
        KySu("KS02", "Pham Thi D", 1992, 3.5)            # Hệ số 3.5
    ]

    print("--- BẢNG LƯƠNG TOÀN CÔNG TY ---")
    # In danh sách bằng list comprehension
    [print(nv) for nv in ds_nhan_vien]
    
    # Tính tổng lương bằng comprehension
    tong_luong = sum(nv.tinh_luong() for nv in ds_nhan_vien)
        
    print(f"\n=> TỔNG TIỀN LƯƠNG PHẢI TRẢ: {tong_luong:,.0f} VNĐ")

    print("\n--- DANH SÁCH KỸ SƯ (Lọc riêng) ---")
    # Lọc kỹ sư bằng list comprehension
    ds_ky_su = [nv for nv in ds_nhan_vien if isinstance(nv, KySu)]
    [print(f"- {nv.ho_ten} (Hệ số: {nv.he_so_luong})") for nv in ds_ky_su]

if __name__ == "__main__":
    main()
