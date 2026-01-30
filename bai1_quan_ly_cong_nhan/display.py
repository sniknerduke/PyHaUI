def in_dong_ke():
    print("+" + "-"*10 + "+" + "-"*20 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")

def in_header():
    print(f"|{'Ma CN':^10}|{'Ho Ten':^20}|{'Luong CB':^15}|{'Phu Cap':^15}|{'Tong TN':^15}|")

def in_mot_cong_nhan(cn):
    print(f"|{cn[0]:^10}|{cn[1]:^20}|{cn[5]:>14,} |{cn[4]:>14,} |{cn[6]:>14,} |")

def in_bang_cong_nhan(ds_cong_nhan):
    print("\nDANH SÁCH CÔNG NHÂN:")
    in_dong_ke()
    in_header()
    in_dong_ke()
    for cn in ds_cong_nhan:
        in_mot_cong_nhan(cn)
    in_dong_ke()

def in_cong_nhan_thu_nhap_cao_nhat(ds_cong_nhan, max_thu_nhap):
    print("Các công nhân có thu nhập cao nhất:")
    for cn in ds_cong_nhan:
        if cn[6] == max_thu_nhap:
            print(f"- {cn[1]} (Mã: {cn[0]})")
