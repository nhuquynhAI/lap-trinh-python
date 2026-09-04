# Bài tap 4.1-Khai bao va tinh bat bien
toa_do = (3, 5)
print(toa_do)
print(type(toa_do))
# Thu thay doi phan tu trong Tuple
# toa_do[0] = 10
# Bài tap 4.2 - Unpacking Tuple
toa_do = (3, 5)
x, y = toa_do
print("x =", x, "- y =", y)
# Doi gia tri 2 bien bang unpacking
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)
# Bài tap 4.3 - Tra ve nhieu gia tri
c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")
#---------------------------------------------------
# Hoat dong 5-Van dung Tuple
# Tinh khoang cach giua cac diem
import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b
khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(
    f"Khoang cach giua {diem_a} va {diem_b} la: "
    f"{round(khoang_cach, 2)}"
)
# Tao danh sach cac diem
cac_diem = [(0, 0), (3, 4), (6, 8)]
# Tinh khoang cach cua tung diem so voi goc toa do
print("Khoang cach cua cac diem so voi goc toa do:")
for x, y in cac_diem:
    khoang_cach = math.sqrt(x ** 2 + y ** 2)
    print(f"Diem ({x}, {y}): {round(khoang_cach, 2)}")