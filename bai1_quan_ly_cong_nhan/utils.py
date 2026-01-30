def tim_cong_nhan_thu_nhap_cao_nhat(ds_cong_nhan):
    if not ds_cong_nhan:
        return []
    max_thu_nhap = max(cn[6] for cn in ds_cong_nhan)
    return [cn for cn in ds_cong_nhan if cn[6] == max_thu_nhap]

def loc_cong_nhan_thoa_dieu_kien(ds_cong_nhan, muc_thu_nhap_yeu_cau=15200000):
    ket_qua = []
    for cn in ds_cong_nhan:
        dk_khong_bang_0 = (cn[5] > 0) and (cn[4] > 0)
        dk_tong_thu_nhap = (cn[6] > muc_thu_nhap_yeu_cau)
        if dk_khong_bang_0 and dk_tong_thu_nhap:
            ket_qua.append(cn)
    return ket_qua
