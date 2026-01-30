from abc import ABC, abstractmethod

# 1. Lớp Trừu tượng (Khuôn mẫu)
class QuanLyNhapXuat(ABC):
    @abstractmethod
    def nhap_thong_tin(self):
        pass

    @abstractmethod
    def xuat_thong_tin(self):
        pass

# 2. Lớp Nhà Cung Cấp
class NhaCungCap(QuanLyNhapXuat):
    def __init__(self, ma_so="", ten="", dia_chi=""):
        self.ma_so = ma_so
        self.ten = ten
        self.dia_chi = dia_chi

    def nhap_thong_tin(self):
        print("--- Nhập thông tin Nhà cung cấp ---")
        self.ma_so = input("Mã số NCC: ")
        self.ten = input("Tên NCC: ")
        self.dia_chi = input("Địa chỉ: ")

    def xuat_thong_tin(self):
        print(f"Mã số: {self.ma_so:<15} Tên NCC: {self.ten}")
        print(f"Địa chỉ: {self.dia_chi}")

# 3. Lớp Mặt Hàng
class MatHang(QuanLyNhapXuat):
    def __init__(self, ten_hang="", don_gia=0.0, so_luong=0):
        self.ten_hang = ten_hang
        self.don_gia = don_gia
        self.so_luong = so_luong

    @property
    def thanh_tien(self):
        return self.don_gia * self.so_luong

    def nhap_thong_tin(self):
        self.ten_hang = input("Tên hàng: ")
        self.don_gia = float(input("Đơn giá: "))
        self.so_luong = int(input("Số lượng: "))

    def xuat_thong_tin(self):
        # In 1 dòng cho bảng
        print(f"{self.ten_hang:<20} {self.don_gia:<10,.0f} {self.so_luong:<10} {self.thanh_tien:<15,.0f}")

# 4. Lớp Phiếu Nhập (Lớp chính)
class PhieuNhap(QuanLyNhapXuat):
    def __init__(self):
        self.ma_phieu = ""
        self.ngay_lap = ""
        # HỢP THÀNH: Phiếu "có" 1 Nhà cung cấp và "có" nhiều Mặt hàng
        self.ncc = NhaCungCap()
        self.ds_hang = []

    def nhap_thong_tin(self):
        print("\n=== NHẬP PHIẾU ===")
        self.ma_phieu = input("Mã phiếu: ")
        self.ngay_lap = input("Ngày lập: ")
        
        # Nhập NCC
        self.ncc.nhap_thong_tin()
        
        # Nhập hàng
        n = int(input("Nhập số lượng mặt hàng: "))
        for i in range(n):
            print(f"-> Nhập hàng thứ {i+1}:")
            mh = MatHang()
            mh.nhap_thong_tin()
            self.ds_hang.append(mh)

    def xuat_thong_tin(self):
        print("\n" + "="*60)
        print(f"{'PHIẾU NHẬP HÀNG':^60}")
        print(f"Mã phiếu: {self.ma_phieu:<20} Ngày lập: {self.ngay_lap}")
        
        # Xuất thông tin đối tượng NCC
        self.ncc.xuat_thong_tin()
        
        print("-" * 60)
        print(f"{'Tên hàng':<20} {'Đơn giá':<10} {'Số lượng':<10} {'Thành tiền':<15}")
        print("-" * 60)
        
        # In danh sách hàng bằng list comprehension
        [mh.xuat_thong_tin() for mh in self.ds_hang]
        
        # Tính tổng tiền bằng comprehension
        tong_tien = sum(mh.thanh_tien for mh in self.ds_hang)
            
        print("-" * 60)
        print(f"{'Cộng thành tiền:':<42} {tong_tien:,.0f} VNĐ")
        print("="*60)

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    # Khởi tạo
    phieu = PhieuNhap()
    
    # Nhập
    phieu.nhap_thong_tin()
    
    # Xuất
    phieu.xuat_thong_tin()

if __name__ == "__main__":
    main()
