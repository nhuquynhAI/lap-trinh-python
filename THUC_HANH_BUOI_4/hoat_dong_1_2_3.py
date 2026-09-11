#BÀI TẬP 1.1 - Khai báo và Truy xuất
#sinh_vien = {
#    "ho_ten": "Nguyen Van A",
#    "nam_sinh": 2004,
#    "diem_tb": 8.5
#}
#print("Họ tên:", sinh_vien["ho_ten"])
#print("Điểm trung bình:", sinh_vien.get("diem_tb"))
#print("Lớp:", sinh_vien.get("lop", "Chua co"))
#------------------------------------------------
#BÀI TẬP 1.2 
#sinh_vien["lop"] = "CNTT01"
#sinh_vien["diem_tb"] = 9.0
#print("\nSau khi thêm lớp và sửa điểm:")
#print(sinh_vien)
#diem_cu = sinh_vien.pop("diem_tb")
#print("\nSau khi xóa điểm:")
#print(sinh_vien)
#print("Điểm đã xóa:", diem_cu)
#sinh_vien.update({
#    "nam_sinh": 2003,
#    "email": "a@example.com"
#})
#print("\nSau khi update:")
#print(sinh_vien)
#------------------------------------------
#Bài tập 2
diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}
print("\n===== DANH SÁCH MÔN HỌC =====")
for mon in diem_mon_hoc.keys():
    print(mon)
print("\n===== DANH SÁCH ĐIỂM =====")
for diem in diem_mon_hoc.values():
    print(diem)
print("\n===== MÔN VÀ ĐIỂM =====")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
diem_trung_binh = round(tong_diem / len(diem_mon_hoc), 2)
print("\nĐiểm trung bình:", diem_trung_binh)
#----------------------------------------------
#BÀI TẬP 3.1
#diem_cong_diem = {
#    mon: round(diem + 0.5, 2)
#    for mon, diem in diem_mon_hoc.items()
#}
#print("\nĐiểm sau khi cộng 0.5:")
#print(diem_cong_diem)
#ten_mon_viet_hoa = {
#    mon.upper(): diem
#    for mon, diem in diem_mon_hoc.items()
#}
#print("\nTên môn viết hoa:")
#print(ten_mon_viet_hoa)
#------------------------------------------
#BÀI TẬP 3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print("\n===== SET =====")
print("Môn học chung 2 học kỳ:")
print(mon_hoc_ky1 & mon_hoc_ky2)
print("Tất cả môn học của 2 học kỳ:")
print(mon_hoc_ky1 | mon_hoc_ky2)
print("Môn chỉ có ở học kỳ 1:")
print(mon_hoc_ky1 - mon_hoc_ky2)