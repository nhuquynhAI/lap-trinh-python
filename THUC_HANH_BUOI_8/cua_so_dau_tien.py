import tkinter as tk 

cua_so = tk.Tk() 
cua_so.title("Ung dung demo") 
cua_so.geometry("400x300") 

# Yeu cau: Thay doi thu resizable(True, False)
#cua_so.resizable(True, False) # Kéo rộng được (True), không kéo cao được (False)

#nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16)) 
#nhan.pack(pady=20) 

#cua_so.mainloop()
#----------------------
#Hoạt động 2
khung_tren = tk.Frame(cua_so, bg="lightblue", height=100) 
khung_tren.pack(fill="x") 

khung_duoi = tk.Frame(cua_so, bg="lightyellow") 
khung_duoi.pack(fill="both", expand=True) 

tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack(pady=10) 
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10) 

cua_so.mainloop()