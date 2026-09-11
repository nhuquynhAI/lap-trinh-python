#BÀI TẬP 7
quan_ly_diem = {
    "Nguyen Van An": [8.0, 7.5, 9.0],
    "Tran Thi Bích": [6.0, 6.5, 5.5],
    "Le Van Cảnh": [9.0, 9.5, 8.5]
}
# Thêm sinh viên mới
quan_ly_diem["Pham Thi Duyên"] = [7.0, 8.0, 7.5]
# Sửa điểm môn đầu tiên của một sinh viên
quan_ly_diem["Tran Thi Bích"][0] = 7.0
# Tạo Dictionary lưu điểm trung bình
diem_trung_binh = {}
for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(
        sum(danh_sach_diem) / len(danh_sach_diem),
        2
    )
# In bảng điểm trung bình
print("BANG DIEM TRUNG BINH:")
for ho_ten, dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    print(
        f"{ho_ten:<15} - DTB: {dtb:<5} "
        f"- Dat loai Gioi? {dat_loai_gioi}"
    )