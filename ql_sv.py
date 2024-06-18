# Name: Chử Quang Vinh  
# Student ID: 20227074
# Class: 150327
# Project: 05 - Chương trình quản lí sinh viên
# Date: 06/06/2024

import datetime 
from models import SinhVien, HocPhan, Diem
from xu_ly_du_lieu import doc_du_lieu, ghi_du_lieu
from giao_dien import them_moi_sinh_vien, sua_sinh_vien, xoa_sinh_vien, \
                         them_moi_hoc_phan, sua_hoc_phan, xoa_hoc_phan, \
                         them_moi_diem, sua_diem, xoa_diem, in_bang_diem, clear_entry
import tkinter as tk
from tkinter import ttk

def main():
    global danh_sach_sv, danh_sach_hp, danh_sach_diem
    danh_sach_sv = doc_du_lieu("SV.bin")
    danh_sach_hp = doc_du_lieu("HP.bin")
    danh_sach_diem = doc_du_lieu("Diem.bin")

    global root
    root = tk.Tk()
    root.title("Quản lý sinh viên")
    root.geometry("900x550")
    root.configure(bg="#f0f0f0")

    style = ttk.Style()
    style.configure("TNotebook", background="#f0f0f0")
    style.configure("TNotebook.Tab", padding=(20, 10), font=("Arial", 12))
    style.map(
        "TNotebook.Tab",
        background=[("selected", "#0078d7")],
        foreground=[("selected", "white")],
    )

    # --- Tạo Frame chính ---
    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(fill="both", expand=True)

    # --- Tạo Notebook trong Frame chính ---
    notebook = ttk.Notebook(main_frame)
    notebook.pack(pady=10, padx=10, fill="both", expand=True)

    # --- Các Tab ---
    tab_sv = tk.Frame(notebook, bg="#f0f0f0")
    tab_hp = tk.Frame(notebook, bg="#f0f0f0")
    tab_diem = tk.Frame(notebook, bg="#f0f0f0")
    tab_in_diem = tk.Frame(notebook, bg="#f0f0f0")

    notebook.add(tab_sv, text="Sinh Viên")
    notebook.add(tab_hp, text="Học Phần")
    notebook.add(tab_diem, text="Điểm")
    notebook.add(tab_in_diem, text="In Bảng Điểm")

    # --- Frame chứa button ---
    btn_frame_sv = tk.Frame(tab_sv, bg="#f0f0f0")
    btn_frame_hp = tk.Frame(tab_hp, bg="#f0f0f0")
    btn_frame_diem = tk.Frame(tab_diem, bg="#f0f0f0")

    btn_frame_sv.pack(pady=10)
    btn_frame_hp.pack(pady=10)
    btn_frame_diem.pack(pady=10)

    # --- Frame chứa thông báo ---
    thong_bao_frame = tk.Frame(main_frame, bg="#f0f0f0")
    thong_bao_frame.pack(pady=10)

    global thong_bao_label
    thong_bao_label = tk.Label(
        thong_bao_frame, text="", font=("Arial", 12), bg="#f0f0f0"
    )
    thong_bao_label.pack()

    # --- Chức năng cập nhật thông báo ---
    def hien_thong_bao(message):
        global thong_bao_label
        thong_bao_label.config(text=message)

    # --- Các Button (thêm chức năng hiển thị thông báo) ---
    button_them_sv = tk.Button(
        btn_frame_sv,
        text="Thêm Sinh Viên",
        command=lambda: them_moi_sinh_vien(danh_sach_sv, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#00a36c",
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_sv = tk.Button(
        btn_frame_sv,
        text="Sửa Sinh Viên",
        command=lambda: sua_sinh_vien(danh_sach_sv, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#0078d7",
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_sv = tk.Button(
        btn_frame_sv,
        text="Xóa Sinh Viên",
        command=lambda: xoa_sinh_vien(danh_sach_sv, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#c42b1c",
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_them_hp = tk.Button(
        btn_frame_hp,
        text="Thêm Học Phần",
        command=lambda: them_moi_hoc_phan(danh_sach_hp, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#00a36c",
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_hp = tk.Button(
        btn_frame_hp,
        text="Sửa Học Phần",
        command=lambda: sua_hoc_phan(danh_sach_hp, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#0078d7",
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_hp = tk.Button(
        btn_frame_hp,
        text="Xóa Học Phần",
        command=lambda: xoa_hoc_phan(danh_sach_hp, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#c42b1c",
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_them_diem = tk.Button(
        btn_frame_diem,
        text="Thêm Điểm",
        command=lambda: them_moi_diem(danh_sach_diem, danh_sach_sv, danh_sach_hp, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#00a36c",
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_diem = tk.Button(
        btn_frame_diem,
        text="Sửa Điểm",
        command=lambda: sua_diem(danh_sach_diem, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#0078d7",
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_diem = tk.Button(
        btn_frame_diem,
        text="Xóa Điểm",
        command=lambda: xoa_diem(danh_sach_diem, hien_thong_bao, root),
        font=("Arial", 12),
        bg="#c42b1c",
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_in_diem = tk.Button(
        tab_in_diem,
        text="Chọn sinh viên để in bảng điểm",
        command=lambda: in_bang_diem(
            danh_sach_diem, danh_sach_sv, danh_sach_hp, hien_thong_bao, root
        ),
        font=("Arial", 12),
        bg="#2b88d8",
        fg="white",
        activebackground="#2060a5",
        activeforeground="white",
        padx=10,
        pady=5,
    )

    # --- Đặt vị trí button ---
    button_them_sv.pack(side="left", padx=5)
    button_sua_sv.pack(side="left", padx=5)
    button_xoa_sv.pack(side="left", padx=5)
    button_them_hp.pack(side="left", padx=5)
    button_sua_hp.pack(side="left", padx=5)
    button_xoa_hp.pack(side="left", padx=5)
    button_them_diem.pack(side="left", padx=5)
    button_sua_diem.pack(side="left", padx=5)
    button_xoa_diem.pack(side="left", padx=5)
    button_in_diem.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()