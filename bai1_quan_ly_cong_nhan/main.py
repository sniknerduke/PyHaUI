import input_handler
import display
import utils

def main():
    print("--- BÀI 1: QUẢN LÝ CÔNG NHÂN ---")
    
    ds_cong_nhan = input_handler.nhap_danh_sach_cong_nhan()
    
    display.in_bang_cong_nhan(ds_cong_nhan)
    
    # Công nhân có thu nhập cao nhất
    ds_thu_nhap_cao_nhat = utils.tim_cong_nhan_thu_nhap_cao_nhat(ds_cong_nhan)
    print("\nCÔNG NHÂN CÓ THU NHẬP CAO NHẤT:")
    display.in_bang_cong_nhan(ds_thu_nhap_cao_nhat)
    
    # Công nhân thỏa điều kiện
    ds_thoa_dk = utils.loc_cong_nhan_thoa_dieu_kien(ds_cong_nhan)
    print(f"\nCÔNG NHÂN THỎA ĐIỀU KIỆN (Thu nhập > 15.2tr & không khoản nào bằng 0): {len(ds_thoa_dk)} người")
    display.in_bang_cong_nhan(ds_thoa_dk)

if __name__ == "__main__":
    main()
