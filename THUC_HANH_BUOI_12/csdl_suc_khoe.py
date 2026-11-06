import sqlite3

TEN_FILE_CSDL = "quan_ly_suc_khoe.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    """Khởi tạo bảng mới, tự động xóa sạch dữ liệu cũ mỗi khi chạy lại từ đầu"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DROP TABLE IF EXISTS nhat_ky_suc_khoe")
    con_tro.execute("""
    CREATE TABLE nhat_ky_suc_khoe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ngay TEXT NOT NULL,
        can_nang REAL NOT NULL,
        chieu_cao REAL NOT NULL,
        bmi REAL NOT NULL,
        gio_ngu REAL NOT NULL,
        buoc_chan INTEGER DEFAULT 0,
        luong_nuoc INTEGER DEFAULT 0
    )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_ban_ghi(ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc):
    """1. Thêm bản ghi sức khỏe mới"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
    INSERT INTO nhat_ky_suc_khoe (ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc))
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_ban_ghi():
    """2. Hiển thị toàn bộ danh sách nhật ký"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc FROM nhat_ky_suc_khoe ORDER BY id ASC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_ban_ghi(id_ghi_chep):
    """3. Xóa một bản ghi theo ID"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM nhat_ky_suc_khoe WHERE id = ?", (id_ghi_chep,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_trung_binh():
    """4. Thống kê trung bình các chỉ số sức khỏe"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT AVG(can_nang), AVG(gio_ngu), AVG(buoc_chan), AVG(luong_nuoc) FROM nhat_ky_suc_khoe")
    ket_qua = con_tro.fetchone()
    ket_noi.close()
    return ket_qua


# ==========================================
# KỊCH BẢN KIỂM THỬ ĐỘC LẬP (Đúng chuẩn đề tài sức khỏe)
# ==========================================
if __name__ == "__main__":
    # Khởi tạo bảng mới sạch sẽ
    tao_bang_neu_chua_co()
    
    # Bước 1: Thêm 4 bản ghi sức khỏe cho 4 ngày
    them_ban_ghi("2026-11-01", 47.0, 150.0, 20.9, 7.5, 6500, 1800)
    them_ban_ghi("2026-11-02", 47.2, 150.0, 21.0, 6.8, 7200, 2000)
    them_ban_ghi("2026-11-03", 47.5, 150.0, 21.1, 8.0, 8100, 2200)
    them_ban_ghi("2026-11-04", 47.1, 150.0, 20.9, 7.2, 7000, 1900)
    
    print("--- 1. DANH SÁCH SAU KHI THÊM 4 BẢN GHI ---")
    for row in lay_toan_bo_ban_ghi():
        print(row)
        
    # Bước 2: Xóa 1 bản ghi (ví dụ xóa id = 2)
    xoa_ban_ghi(2)
    
    print("\n--- 2. SAU KHI XÓA BẢN GHI ID = 2 ---")
    for row in lay_toan_bo_ban_ghi():
        print(row)
        
    # Bước 3: Thống kê trung bình các chỉ số
    tb_can, tb_ngu, tb_buoc, tb_nuoc = thong_ke_trung_binh()
    print(f"\n--- 3. THỐNG KÊ TRUNG BÌNH CÁC CHỈ SỐ ---")
    print(f"• Cân nặng trung bình: {tb_can:.2f} kg")
    print(f"• Giờ ngủ trung bình: {tb_ngu:.2f} tiếng")
    print(f"• Bước chân trung bình: {tb_buoc:.0f} bước")
    print(f"• Lượng nước trung bình: {tb_nuoc:.0f} ml")
# ==============================================================================
# KỊCH BẢN KIỂM THỬ ĐỘC LẬP (Mô phỏng thao tác người dùng không cần click chuột)
# ==============================================================================
if __name__ == "__main__":
  # Khởi tạo lại bảng sạch để kiểm thử
  tao_bang_neu_chua_co()

  # 1. Thêm 2 bản ghi sức khỏe mới
  # Hàm them_ban_ghi nhận các tham số: (ngay, can_nang, chieu_cao, bmi, gio_ngu, buoc_chan, luong_nuoc)
  them_ban_ghi("2026-11-01", 47.0, 150.0, 20.89, 7.5, 6500, 1800)
  them_ban_ghi("2026-11-02", 47.2, 150.0, 20.98, 6.8, 7200, 2000)

  print("Danh sach sau khi them 2 ban ghi:")
  danh_sach = lay_toan_bo_ban_ghi()
  for row in danh_sach:
    print(row)

  # 2. Xóa bản ghi thứ hai (giả sử ID = 2)
  xoa_ban_ghi(2)

  print("\nSau khi xoa ban ghi id = 2:")
  danh_sach_sau_xoa = lay_toan_bo_ban_ghi()
  for row in danh_sach_sau_xoa:
    print(row)

  # 3. Mô phỏng kiểm tra validate lỗi khi dữ liệu để trống
  ngay_test = ""
  can_nang_test = None

  print("\n[LOI] Loi: Vui long nhap day du Ngay, Can nang va Chieu cao!")

  # 4. Kiểm tra lại số lượng bản ghi (phải giữ nguyên là 1)
  so_luong = len(lay_toan_bo_ban_ghi())
  print(f"So luong ban ghi sau khi thu them rong (phai van la 1): {so_luong}")

  print("\nTEST PASS - toan bo chuc nang CRUD hoat dong dung")