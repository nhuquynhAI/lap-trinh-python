# QUAN LY DANH SACH SINH VIEN BANG LIST
danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]
# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))
print("Danh sach sau khi them sinh vien:")
print(danh_sach_sv)
# Xoa sinh vien Binh
danh_sach_sv.remove((7.0, "Binh"))
print("\nDanh sach sau khi xoa Binh:")
print(danh_sach_sv)
# Sua diem cho sinh vien o vi tri 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])
print("\nDanh sach sau khi sua diem:")
print(danh_sach_sv)
# Kiem tra Chi co trong danh sach hay khong
print(
    "\nChi co trong danh sach khong?",
    (9.2, "Chi") in danh_sach_sv
)
# Sap xep tang dan theo diem
danh_sach_sv.sort()
print("\nDanh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")
# Sap xep giam dan theo diem
danh_sach_sv.sort(reverse=True)
print("\nDanh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")