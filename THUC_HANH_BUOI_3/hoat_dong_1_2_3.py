# Bài tập 1.1 - Khai báo & truy cập List
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0])      # Phan tu dau tien
print(diem_so[-1])     # Phan tu cuoi cung
print(diem_so[1:4])    # Cat tu vi tri 1 den truoc vi tri 4
print(diem_so[::2])    # Lay cac phan tu cach nhau 1 vi tri
print(diem_so[::-1])   # Dao nguoc danh sach
# Bài tập 1.2 - Cac phuong thuc thuong dung
ten_sv = ["An", "Binh", "Chi"]
# Them sinh vien vao cuoi danh sach
ten_sv.append("Dung")
# Chen sinh vien vao vi tri 1
ten_sv.insert(1, "Em")
print(ten_sv)
# Xoa sinh vien theo gia tri
ten_sv.remove("Chi")
# Xoa phan tu cuoi danh sach va luu lai gia tri vua xoa
pop_ra = ten_sv.pop()
print(ten_sv, "- da xoa:", pop_ra)
# Sap xep tang dan theo bang chu cai
ten_sv.sort()
print(ten_sv)
# Dao nguoc thu tu hien tai
ten_sv.reverse()
print(ten_sv)
# Noi them mot List khac vao List hien tai
ten_sv.extend(["Giang", "Hoa"])
print(ten_sv)
#---------------------------------------------------
# Bài tập 2.1 - Duyet List bang for
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong = tong + diem
print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))
# Bài tập 2.2 - List long nhau (ma tran)
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# In ra tung hang
for hang in ma_tran:
    print(hang)
# In ra tung phan tu
# Duyet theo hang roi theo cot
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
# Tinh tong tat ca cac phan tu trong ma tran
tong = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong = tong + phan_tu
print("Tong cac phan tu trong ma tran:", tong)
#----------------------------------------------------
# Bài tập 3.1-Loc so chan le
day_so = list(range(1, 21))
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("So chan:", so_chan)
print("So le:", so_le)
# Bài tập 3.2 - Bien doi phan tu
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)