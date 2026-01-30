import input_handler
import display
import utils

def main():
    print("\n" + "="*30 + "\n--- BÀI 2: QUẢN LÝ TỪ ĐIỂN SẢN PHẨM ---")
    
    san_pham = input_handler.nhap_san_pham()
    loai_san_pham = input_handler.nhap_loai_san_pham()
    
    display.in_bang_loai_san_pham(loai_san_pham)
    
    san_pham = utils.kiem_tra_va_cap_nhat_sp(san_pham, "SP01", 100)
    display.in_bang_san_pham(san_pham, "DANH SACH SP SAU KHI CAP NHAT/THEM SP01")
    
    san_pham = utils.xoa_sp_so_luong_0(san_pham)
    display.in_bang_san_pham(san_pham, "DANH SACH SP SAU KHI XOA SP CO SO LUONG 0")
    
    list_ma_sp, list_so_luong = utils.chuyen_dict_sang_list(san_pham)
    
    print(f"\n3 phan tu DAU TIEN cua danh sach ma SP: {utils.lay_n_phan_tu_dau(list_ma_sp)}")
    print(f"3 phan tu CUOI CUNG cua danh sach so luong: {utils.lay_n_phan_tu_cuoi(list_so_luong)}")

if __name__ == "__main__":
    main()
