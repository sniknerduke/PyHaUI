class SanPham:
    def __init__(self, ma_sp, ten_sp, don_gia, so_luong):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.don_gia = don_gia
        self.so_luong = so_luong

    def thanh_tien(self):
        return self.don_gia * self.so_luong

    def __str__(self):
        # In định dạng bảng: Mã (10 ký tự), Tên (20), Giá (15), SL (5), Thành tiền (15)
        return f"{self.ma_sp:<10} {self.ten_sp:<20} {self.don_gia:<15,.0f} {self.so_luong:<5} {self.thanh_tien():<15,.0f}"

class PhieuNhap:
    def __init__(self, ma_phieu, ngay_lap):
        self.ma_phieu = ma_phieu
        self.ngay_lap = ngay_lap
        self.danh_sach_sp = []  # <--- List chứa các đối tượng SanPham

    def them_san_pham(self):
        n = int(input(f"Nhập số lượng mặt hàng cho phiếu {self.ma_phieu}: "))
        for i in range(n):
            print(f"  > Nhập hàng thứ {i + 1}:")
            ma = input("    Mã SP: ")
            ten = input("    Tên SP: ")
            gia = float(input("    Đơn giá: "))
            sl = int(input("    Số lượng: "))
            
            # Tạo đối tượng SanPham và thêm vào list của Phiếu
            sp = SanPham(ma, ten, gia, sl)
            self.danh_sach_sp.append(sp)

    def sap_xep_giam_dan(self):
        # Sắp xếp list danh_sach_sp dựa trên don_gia
        # reverse=True để giảm dần (cao xuống thấp)
        self.danh_sach_sp.sort(key=lambda x: x.don_gia, reverse=True)

    def tinh_tong_tien(self):
        # Dùng comprehension thay vì vòng for
        return sum(sp.thanh_tien() for sp in self.danh_sach_sp)

    def in_phieu(self):
        print("\n" + "="*70)
        print(f"{'PHIẾU NHẬP KHO':^70}")
        print(f"Mã phiếu: {self.ma_phieu:<30} Ngày lập: {self.ngay_lap}")
        print("-" * 70)
        print(f"{'Mã SP':<10} {'Tên Hàng':<20} {'Đơn giá':<15} {'SL':<5} {'Thành tiền':<15}")
        print("-" * 70)
        
        # In danh sách bằng list comprehension
        [print(sp) for sp in self.danh_sach_sp]
            
        print("-" * 70)
        print(f"{'TỔNG CỘNG:':<51} {self.tinh_tong_tien():,.0f} VNĐ")
        print("="*70)

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    # 1. Tạo phiếu
    print("--- KHỞI TẠO PHIẾU ---")
    ma = input("Nhập mã phiếu: ")
    ngay = input("Nhập ngày lập: ")
    phieu = PhieuNhap(ma, ngay)
    
    # 2. Nhập hàng vào phiếu
    phieu.them_san_pham()
    
    # 3. Sắp xếp
    phieu.sap_xep_giam_dan()
    
    # 4. In kết quả
    print("\n--- KẾT QUẢ SAU KHI SẮP XẾP ---")
    phieu.in_phieu()

if __name__ == "__main__":
    main()
