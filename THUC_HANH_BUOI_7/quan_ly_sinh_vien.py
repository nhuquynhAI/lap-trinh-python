# KHOI TAO DU LIEU
danh_sach_sinh_vien = [
    {"ma_sv": "SV001","ho_ten": "Nguyen Van A","tuoi": 20,"lop": "DH14C1","diem_tb": 8.5},
    {"ma_sv": "SV002","ho_ten": "Tran Thi B","tuoi": 19,"lop": "DH14C1","diem_tb": 7.8},
    {"ma_sv": "SV003","ho_ten": "Le Van C","tuoi": 20,"lop": "DH14C2","diem_tb": 9.0}
]

# ==========================================
# HIEN THI DANH SACH TOAN BO SINH VIEN
def hien_thi_danh_sach():

    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien dang trong.")
        return

    print("\n" + "=" * 80)
    print("DANH SACH TOAN BO SINH VIEN")
    print("=" * 80)

    print(
        f"{'Ma SV':<10}"
        f"{'Ho ten':<25}"
        f"{'Tuoi':<8}"
        f"{'Lop':<12}"
        f"{'Diem TB':<10}"
    )

    print("-" * 80)

    for sinh_vien in danh_sach_sinh_vien:
        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<25}"
            f"{sinh_vien['tuoi']:<8}"
            f"{sinh_vien['lop']:<12}"
            f"{sinh_vien['diem_tb']:<10.2f}"
        )

    print("=" * 80)

# ==========================================
# TIM KIEM SINH VIEN THEO MA

def tim_sinh_vien_theo_ma(ma_sv):

    for sinh_vien in danh_sach_sinh_vien:

        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien

    return None


def tim_kiem_sinh_vien():

    ma_sv = input(
        "Nhap ma sinh vien can tim: "
    ).strip().upper()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:

        print("-> Khong tim thay sinh vien.")

    else:

        print("\n" + "=" * 50)
        print("THONG TIN SINH VIEN")
        print("=" * 50)

        print(f"Ma sinh vien : {sinh_vien['ma_sv']}")
        print(f"Ho ten       : {sinh_vien['ho_ten']}")
        print(f"Tuoi         : {sinh_vien['tuoi']}")
        print(f"Lop          : {sinh_vien['lop']}")
        print(f"Diem trung binh: {sinh_vien['diem_tb']:.2f}")

        print("=" * 50)


# ==========================================
# THEM SINH VIEN MOI

def them_sinh_vien():

    print("\n" + "=" * 50)
    print("THEM SINH VIEN MOI")
    print("=" * 50)

    ma_sv = input(
        "Nhap ma sinh vien: "
    ).strip().upper()

    # Kiem tra ma sinh vien da ton tai
    if tim_sinh_vien_theo_ma(ma_sv) is not None:

        print("-> Ma sinh vien da ton tai.")
        return

    ho_ten = input(
        "Nhap ho ten: "
    ).strip()

    tuoi = nhap_so_nguyen(
        "Nhap tuoi: "
    )

    lop = input(
        "Nhap lop: "
    ).strip().upper()

    diem_tb = nhap_diem(
        "Nhap diem trung binh: "
    )

    sinh_vien_moi = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "lop": lop,
        "diem_tb": diem_tb
    }

    danh_sach_sinh_vien.append(
        sinh_vien_moi
    )

    print("-> Da them sinh vien thanh cong.")


# ==========================================
# CAP NHAT THONG TIN SINH VIEN

def cap_nhat_sinh_vien():

    print("\n" + "=" * 50)
    print("CAP NHAT THONG TIN SINH VIEN")
    print("=" * 50)

    ma_sv = input(
        "Nhap ma sinh vien can cap nhat: "
    ).strip().upper()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:

        print("-> Khong tim thay sinh vien.")
        return

    print("Nhap thong tin moi:")

    sinh_vien["ho_ten"] = input(
        "Nhap ho ten moi: "
    ).strip()

    sinh_vien["tuoi"] = nhap_so_nguyen(
        "Nhap tuoi moi: "
    )

    sinh_vien["lop"] = input(
        "Nhap lop moi: "
    ).strip().upper()

    sinh_vien["diem_tb"] = nhap_diem(
        "Nhap diem trung binh moi: "
    )

    print("-> Da cap nhat thong tin thanh cong.")


# ==========================================
# XOA SINH VIEN

def xoa_sinh_vien():

    print("\n" + "=" * 50)
    print("XOA SINH VIEN")
    print("=" * 50)

    ma_sv = input(
        "Nhap ma sinh vien can xoa: "
    ).strip().upper()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:

        print("-> Khong tim thay sinh vien.")
        return

    danh_sach_sinh_vien.remove(
        sinh_vien
    )

    print("-> Da xoa sinh vien thanh cong.")


# ==========================================
# THONG KE KET QUA HOC TAP

def thong_ke_sinh_vien():

    if len(danh_sach_sinh_vien) == 0:

        print("-> Chua co sinh vien de thong ke.")
        return

    tong_diem = 0

    for sinh_vien in danh_sach_sinh_vien:

        tong_diem += sinh_vien["diem_tb"]

    diem_trung_binh = (
        tong_diem / len(danh_sach_sinh_vien)
    )

    print("\n" + "=" * 60)
    print("THONG KE KET QUA HOC TAP")
    print("=" * 60)

    print(
        f"So luong sinh vien: "
        f"{len(danh_sach_sinh_vien)}"
    )

    print(
        f"Diem trung binh chung: "
        f"{diem_trung_binh:.2f}"
    )

    print("\nDIEM TRUNG BINH CUA CAC SINH VIEN:")
    print("-" * 60)

    for sinh_vien in danh_sach_sinh_vien:

        print(
            f"{sinh_vien['ma_sv']} - "
            f"{sinh_vien['ho_ten']} - "
            f"{sinh_vien['diem_tb']:.2f}"
        )

    print("=" * 60)


# ==========================================
# HAM HO TRO NHAP SO NGUYEN AN TOAN

def nhap_so_nguyen(loi_nhac):

    while True:

        try:

            return int(input(loi_nhac))

        except ValueError:

            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so nguyen."
            )


# ==========================================
# HAM HO TRO NHAP DIEM AN TOAN

def nhap_diem(loi_nhac):

    while True:

        try:

            diem = float(input(loi_nhac))

            if 0 <= diem <= 10:

                return diem

            print(
                "-> Diem phai nam trong khoang "
                "tu 0 den 10."
            )

        except ValueError:

            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so."
            )


# ==========================================
# MENU CHINH

def hien_thi_menu():

    print("\n" + "=" * 50)
    print("           QUAN LY SINH VIEN")
    print("=" * 50)

    print("1. Hien thi danh sach sinh vien")
    print("2. Tim kiem sinh vien")
    print("3. Them sinh vien moi")
    print("4. Cap nhat thong tin sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke ket qua hoc tap")
    print("0. Thoat")

    print("=" * 50)


# ==========================================
# VONG LAP MENU CHINH

def chay_chuong_trinh():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon cua ban: "
        )

        if lua_chon == "1":

            hien_thi_danh_sach()

        elif lua_chon == "2":

            tim_kiem_sinh_vien()

        elif lua_chon == "3":

            them_sinh_vien()

        elif lua_chon == "4":

            cap_nhat_sinh_vien()

        elif lua_chon == "5":

            xoa_sinh_vien()

        elif lua_chon == "6":

            thong_ke_sinh_vien()

        elif lua_chon == "0":

            print("-> Ket thuc chuong trinh.")
            break

        else:

            print(
                "-> Lua chon khong hop le, "
                "vui long chon lai."
            )


# ==========================================
# CHUONG TRINH CHINH

if __name__ == "__main__":

    chay_chuong_trinh()