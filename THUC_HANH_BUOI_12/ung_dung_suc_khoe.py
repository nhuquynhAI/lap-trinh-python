import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_suc_khoe as db

class UngDungQuanLySucKhoe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng Quản lý Sức khỏe Cá nhân")
        self.geometry("740x550")
        self.resizable(False, False)
        
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(self, text=" Nhập chỉ số theo dõi sức khỏe hằng ngày ", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        # Hàng 0
        tk.Label(khung_nhap, text="Ngày (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ngay = tk.Entry(khung_nhap, width=18)
        self.o_nhap_ngay.insert(0, datetime.date.today().strftime("%Y-%m-%d"))
        self.o_nhap_ngay.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Cân nặng (kg):").grid(row=0, column=2, sticky="w", pady=5)
        self.o_nhap_can_nang = tk.Entry(khung_nhap, width=18)
        self.o_nhap_can_nang.grid(row=0, column=3, padx=5, pady=5)

        # Hàng 1
        tk.Label(khung_nhap, text="Chiều cao (cm):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_chieu_cao = tk.Entry(khung_nhap, width=18)
        self.o_nhap_chieu_cao.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Giờ ngủ (tiếng):").grid(row=1, column=2, sticky="w", pady=5)
        self.o_nhap_gio_ngu = tk.Entry(khung_nhap, width=18)
        self.o_nhap_gio_ngu.grid(row=1, column=3, padx=5, pady=5)

        # Hàng 2
        tk.Label(khung_nhap, text="Số bước chân:").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_buoc_chan = tk.Entry(khung_nhap, width=18)
        self.o_nhap_buoc_chan.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Nước uống (ml):").grid(row=2, column=2, sticky="w", pady=5)
        self.o_nhap_luong_nuoc = tk.Entry(khung_nhap, width=18)
        self.o_nhap_luong_nuoc.grid(row=2, column=3, padx=5, pady=5)

        # Nút Thêm
        tk.Button(khung_nhap, text="Thêm bản ghi sức khỏe", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.xu_ly_them).grid(row=3, column=0, columnspan=4, pady=10, sticky="we")

        # Khung danh sách Listbox
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_data = tk.Listbox(khung_danh_sach, width=100, height=12, font=("Consolas", 9))
        self.listbox_data.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_data.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_data.config(yscrollcommand=thanh_cuon.set)

        # Khung nút chức năng bên dưới
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xóa bản ghi đã chọn", bg="#f44336", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Xem biểu đồ thống kê", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_ve_bieu_do).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_data.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_ban_ghi()
        for item in self.danh_sach_hien_tai:
            id_rec, ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc = item
            self.listbox_data.insert(
                tk.END, 
                f"[{ngay}]  Cân nặng: {can_nang}kg  |  Chiều cao: {chieu_cao}cm  |  BMI: {bmi:.1f}  |  Ngủ: {gio_ngu}h  |  Bước: {buoc_chan}  |  Nước: {luong_nuoc}ml"
            )

    def xu_ly_them(self):
        try:
            ngay = self.o_nhap_ngay.get().strip()
            can_nang = float(self.o_nhap_can_nang.get().strip())
            chieu_cao = float(self.o_nhap_chieu_cao.get().strip())
            gio_ngu = float(self.o_nhap_gio_ngu.get().strip() or 0)
            buoc_chan = int(self.o_nhap_buoc_chan.get().strip() or 0)
            luong_nuoc = int(self.o_nhap_luong_nuoc.get().strip() or 0)

            if not ngay:
                messagebox.showerror("Lỗi", "Vui lòng nhập ngày tháng.")
                return

            # Tự động tính chỉ số BMI
            chieu_cao_m = chieu_cao / 100.0
            bmi = can_nang / (chieu_cao_m ** 2)

            db.them_ban_ghi(ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc)
            self.tai_lai_danh_sach()
            messagebox.showinfo("Thành công", f"Đã lưu bản ghi ngày {ngay}!\nChỉ số BMI: {bmi:.1f}")

            # Xóa sạch ô nhập liệu sau khi thêm thành công
            self.o_nhap_can_nang.delete(0, tk.END)
            self.o_nhap_chieu_cao.delete(0, tk.END)
            self.o_nhap_gio_ngu.delete(0, tk.END)
            self.o_nhap_buoc_chan.delete(0, tk.END)
            self.o_nhap_luong_nuoc.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Lỗi dữ liệu", "Vui lòng nhập đúng định dạng số cho Cân nặng, Chiều cao, Giờ ngủ, Bước chân và Nước uống!")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_data.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một bản ghi trong danh sách để xóa.")
            return
        id_rec = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_ban_ghi(id_rec)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thông báo", "Đã xóa bản ghi thành công.")

    def xu_ly_ve_bieu_do(self):
        du_lieu = db.lay_toan_bo_ban_ghi()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu để vẽ biểu đồ.")
            return

        ds_ngay = [row[1] for row in du_lieu]
        ds_can_nang = [row[2] for row in du_lieu]
        ds_gio_ngu = [row[5] for row in du_lieu]

        fig, ax1 = plt.subplots(figsize=(8, 4.5))

        color = 'tab:red'
        ax1.set_xlabel('Ngày ghi nhận', fontweight='bold')
        ax1.set_ylabel('Cân nặng (kg)', color=color, fontweight='bold')
        ax1.plot(ds_ngay, ds_can_nang, color=color, marker='o', linewidth=2, label='Cân nặng')
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  
        color = 'tab:purple'
        ax2.set_ylabel('Giờ ngủ (tiếng)', color=color, fontweight='bold')
        ax2.plot(ds_ngay, ds_gio_ngu, color=color, marker='^', linestyle='--', linewidth=2, label='Giờ ngủ')
        ax2.tick_params(axis='y', labelcolor=color)

        plt.title('BIỂU ĐỒ THỐNG KÊ CÂN NẶNG VÀ GIỜ NGỦ HẰNG NGÀY', fontsize=11, fontweight='bold')
        fig.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLySucKhoe()
    app.mainloop()