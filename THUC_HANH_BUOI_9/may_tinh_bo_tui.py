import tkinter as tk
from tkinter import messagebox


def them_ky_tu(ky_tu):
    """
    Thêm số hoặc phép toán vào ô hiển thị.
    """
    bien_man_hinh.set(
        bien_man_hinh.get() + ky_tu
    )


def xoa_tat_ca():
    """
    Xóa toàn bộ biểu thức.
    """
    bien_man_hinh.set("")


def xoa_ky_tu_cuoi():
    """
    Xóa ký tự cuối cùng.
    """
    bieu_thuc = bien_man_hinh.get()

    if bieu_thuc:
        bien_man_hinh.set(
            bieu_thuc[:-1]
        )


def tinh_ket_qua():
    """
    Tính kết quả biểu thức.
    """
    bieu_thuc = bien_man_hinh.get()

    if bieu_thuc == "":
        messagebox.showerror(
            "Loi",
            "Vui long nhap bieu thuc."
        )
        return

    try:
        ket_qua = eval(bieu_thuc)

        bien_man_hinh.set(
            str(ket_qua)
        )

    except ZeroDivisionError:
        messagebox.showerror(
            "Loi",
            "Khong the chia cho 0."
        )

    except Exception:
        messagebox.showerror(
            "Loi",
            "Bieu thuc khong hop le."
        )

# TẠO CỬA SỔ
cua_so = tk.Tk()

cua_so.title("May tinh bo tui")

cua_so.geometry("350x500")

cua_so.resizable(False, False)

# BIẾN ĐIỀU KHIỂN
bien_man_hinh = tk.StringVar()

# Ô HIỂN THỊ
o_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_man_hinh,
    font=("Arial", 22),
    justify="right",
    width=18
)

o_hien_thi.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipady=10
)

# CÁC NÚT MÁY TÍNH
# Hàng 1
tk.Button(
    cua_so,
    text="7",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("7")
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="8",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("8")
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="9",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("9")
).grid(row=1, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="/",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("/")
).grid(row=1, column=3, padx=5, pady=5)


# Hàng 2
tk.Button(
    cua_so,
    text="4",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("4")
).grid(row=2, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="5",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("5")
).grid(row=2, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="6",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("6")
).grid(row=2, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="*",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("*")
).grid(row=2, column=3, padx=5, pady=5)


# Hàng 3
tk.Button(
    cua_so,
    text="1",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("1")
).grid(row=3, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text="2",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("2")
).grid(row=3, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="3",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("3")
).grid(row=3, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="-",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("-")
).grid(row=3, column=3, padx=5, pady=5)

# Hàng 4
tk.Button(
    cua_so,
    text="0",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("0")
).grid(row=4, column=0, padx=5, pady=5)

tk.Button(
    cua_so,
    text=".",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu(".")
).grid(row=4, column=1, padx=5, pady=5)

tk.Button(
    cua_so,
    text="=",
    font=("Arial", 16),
    width=5,
    height=2,
    command=tinh_ket_qua
).grid(row=4, column=2, padx=5, pady=5)

tk.Button(
    cua_so,
    text="+",
    font=("Arial", 16),
    width=5,
    height=2,
    command=lambda: them_ky_tu("+")
).grid(row=4, column=3, padx=5, pady=5)

# Hàng 5
tk.Button(
    cua_so,
    text="C",
    font=("Arial", 16),
    width=11,
    height=2,
    command=xoa_tat_ca
).grid(
    row=5,
    column=0,
    columnspan=2,
    padx=5,
    pady=10
)

tk.Button(
    cua_so,
    text="⌫",
    font=("Arial", 16),
    width=11,
    height=2,
    command=xoa_ky_tu_cuoi
).grid(
    row=5,
    column=2,
    columnspan=2,
    padx=5,
    pady=10
)

cua_so.mainloop()