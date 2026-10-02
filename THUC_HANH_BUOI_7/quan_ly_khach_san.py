# 4.1: KHOI TAO DU LIEU
danh_sach_phong = [
    {"ma_phong": "P101", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P102", "loai_phong": "Doi", "gia": 500000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P103", "loai_phong": "VIP", "gia": 900000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "P104", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
]

lich_su_doanh_thu = []
# ==========================================
# 4.2: HIEN THI VA TIM KIEM PHONG

def hien_thi_danh_sach_phong():
    print("\n" + "=" * 75)
    print(
        f"{'Ma phong':<12}"
        f"{'Loai phong':<15}"
        f"{'Gia/dem':<18}"
        f"{'Trang thai':<15}"
        f"{'Khach':<15}"
    )
    print("-" * 75)

    for phong in danh_sach_phong:
        print(
            f"{phong['ma_phong']:<12}"
            f"{phong['loai_phong']:<15}"
            f"{phong['gia']:>12,}      "
            f"{phong['trang_thai']:<15}"
            f"{phong['ten_khach']:<15}"
        )

    print("=" * 75)


def tim_phong_theo_ma(ma_phong):
    for phong in danh_sach_phong:
        if phong["ma_phong"] == ma_phong:
            return phong

    return None


def xem_phong_trong():
    phong_trong = [
        phong for phong in danh_sach_phong
        if phong["trang_thai"] == "Trong"
    ]

    if len(phong_trong) == 0:
        print("-> Hien khong con phong trong nao.")
        return

    print("\n" + "=" * 50)
    print("CAC PHONG DANG TRONG")
    print("-" * 50)

    for phong in phong_trong:
        print(
            f"{phong['ma_phong']} - "
            f"{phong['loai_phong']} - "
            f"{phong['gia']:,} VND/dem"
        )

    print("=" * 50)


# ==========================================
# 4.3: THEM, DAT VA TRA PHONG

def them_phong(ma_phong, loai_phong, gia):
    if tim_phong_theo_ma(ma_phong) is not None:
        print(f"-> Ma phong {ma_phong} da ton tai, khong the them.")
        return

    danh_sach_phong.append({
        "ma_phong": ma_phong,
        "loai_phong": loai_phong,
        "gia": gia,
        "trang_thai": "Trong",
        "ten_khach": ""
    })

    print(f"-> Da them phong {ma_phong} thanh cong.")


def dat_phong(ma_phong, ten_khach):
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Da dat":
        print(f"-> Phong {ma_phong} da co khach, khong the dat.")
        return

    phong["trang_thai"] = "Da dat"
    phong["ten_khach"] = ten_khach

    print(
        f"-> Dat phong {ma_phong} "
        f"cho khach {ten_khach} thanh cong."
    )


def tra_phong(ma_phong, so_dem):
    phong = tim_phong_theo_ma(ma_phong)

    if phong is None:
        print(f"-> Khong tim thay phong {ma_phong}.")
        return

    if phong["trang_thai"] == "Trong":
        print(
            f"-> Phong {ma_phong} dang trong, "
            "khong co khach de tra phong."
        )
        return

    thanh_tien = phong["gia"] * so_dem

    lich_su_doanh_thu.append({
        "ma_phong": ma_phong,
        "ten_khach": phong["ten_khach"],
        "so_dem": so_dem,
        "thanh_tien": thanh_tien
    })

    print(
        f"-> Khach {phong['ten_khach']} "
        f"tra phong {ma_phong} sau {so_dem} dem."
    )

    print(f"-> Tong tien phai thanh toan: {thanh_tien:,} VND")

    phong["trang_thai"] = "Trong"
    phong["ten_khach"] = ""

# ==========================================
# 4.4: THONG KE DOANH THU VA NHAP SO NGUYEN AN TOAN
def thong_ke_doanh_thu():
    if len(lich_su_doanh_thu) == 0:
        print("-> Chua co giao dich tra phong nao.")
        return

    tong_doanh_thu = 0

    print("\n" + "=" * 65)
    print("LICH SU GIAO DICH")
    print("-" * 65)

    for gd in lich_su_doanh_thu:
        print(
            f"{gd['ma_phong']} - "
            f"{gd['ten_khach']} - "
            f"{gd['so_dem']} dem - "
            f"{gd['thanh_tien']:,} VND"
        )

        tong_doanh_thu += gd["thanh_tien"]

    print("-" * 65)
    print(f">>> TONG DOANH THU: {tong_doanh_thu:,} VND")
    print("=" * 65)


def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))

        except ValueError:
            print(
                "-> Du lieu khong hop le, "
                "vui long nhap lai mot so nguyen."
            )


# ==========================================
# 4.5: MENU VA CHUONG TRINH CHINH

def hien_thi_menu():
    print("\n" + "=" * 45)
    print("     QUAN LY DAT PHONG KHACH SAN MINI")
    print("=" * 45)
    print("1. Hien thi danh sach tat ca phong")
    print("2. Xem cac phong dang trong")
    print("3. Them phong moi")
    print("4. Dat phong cho khach")
    print("5. Tra phong / Thanh toan")
    print("6. Thong ke doanh thu")
    print("0. Thoat chuong trinh")
    print("=" * 45)


def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_phong()

        elif lua_chon == "2":
            xem_phong_trong()

        elif lua_chon == "3":
            ma_phong = input(
                "Nhap ma phong moi: "
            ).strip().upper()

            loai_phong = input(
                "Nhap loai phong (Don/Doi/VIP): "
            ).strip().title()

            gia = nhap_so_nguyen(
                "Nhap gia phong/dem: "
            )

            them_phong(ma_phong, loai_phong, gia)

        elif lua_chon == "4":
            ma_phong = input(
                "Nhap ma phong can dat: "
            ).strip().upper()

            ten_khach = input(
                "Nhap ten khach: "
            ).strip().title()

            dat_phong(ma_phong, ten_khach)

        elif lua_chon == "5":
            ma_phong = input(
                "Nhap ma phong can tra: "
            ).strip().upper()

            so_dem = nhap_so_nguyen(
                "Nhap so dem da o: "
            )

            tra_phong(ma_phong, so_dem)

        elif lua_chon == "6":
            thong_ke_doanh_thu()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()