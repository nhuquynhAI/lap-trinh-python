# Bai tap 5
# Nhap thong tin
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")
# Chuan hoa ho ten
ho_ten_chuan = " ".join(ho_ten.split()).title()
# Kiem tra so dien thoai co du 10 ky tu
sdt_hop_le = len(sdt) == 10
# Kiem tra email co ky tu @
email_hop_le = "@" in email
# In ket qua
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")