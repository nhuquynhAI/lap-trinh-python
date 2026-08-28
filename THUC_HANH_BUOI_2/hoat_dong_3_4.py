# Bai tap 3.1 - Cac kieu so va chuyen doi
#so_nguyen = 15
#so_thuc = 4.2
#so_phuc = 3 + 4j
#print(type(so_nguyen))
#print(type(so_thuc))
#print(type(so_phuc))
#print(float(so_nguyen))
#print(int(so_thuc))
# Bai tap 3.2 - Ham built-in xu ly so
#a = -7
#b = 2.6789
#c, d = 17, 5
#print(abs(a))
#print(round(b))
#print(round(b, 2))
#print(pow(c, 2))
#print(divmod(c, d))
# Bai tap 3.3 - Phuong trinh bac hai
#import math
#a, b, c = 1, -3, 2
#delta = b ** 2 - 4 * a * c
#x1 = (-b + math.sqrt(delta)) / (2 * a)
#x2 = (-b - math.sqrt(delta)) / (2 * a)
#print(f"Delta = {delta}")
#print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
# Bai tap 4.1 - Indexing va slicing
#cau = "Lap trinh Python rat thu vi"
#print(cau[0])
#print(cau[-1])
#print(cau[4:10])
#print(cau[:8])
#print(cau[11:])
#print(cau[::-1])
#print(cau == cau[::-1])
# Bai tap 4.2 - Tinh bat bien cua String
#ten = "Nam"
# Neu bo comment dong duoi day thi se bi TypeError
# ten[0] = "T"
#ten_moi = "T" + ten[1:]
#print(ten_moi)
# Bai tap 4.3 - Cac phuong thuc xu ly chuoi
#cau = " Toi dang HOC Python rat vui "
#print(cau.strip())
#print(cau.strip().upper())
#print(cau.strip().lower())
#print(cau.strip().replace("HOC", "hoc"))
#print(cau.strip().split())
#print(len(cau.strip().split()))
#print(cau.count("o"))
#print(cau.find("Python"))
#print(cau.strip().startswith("Toi"))
#print(cau.strip().endswith("vui"))
#print("-".join(["Python", "that", "thu", "vi"]))
# Bai tap 4.4 - Chuan hoa ho ten
ho_ten_tho = " nguyen   van   an "
buoc_1 = ho_ten_tho.strip()
buoc_2 = buoc_1.split()
buoc_3 = " ".join(buoc_2)
ho_ten_sach = buoc_3.title()
print(ho_ten_sach)