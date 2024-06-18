# Name: Chử Quang Vinh  
# Student ID: 20227074
# Class: 150327
# Project: 05 - Chương trình quản lí sinh viên
# Date: 06/06/2024

import datetime
import tkinter as tk
from tkinter import ttk
import os
from models import SinhVien, HocPhan, Diem
from xu_ly_du_lieu import doc_du_lieu, ghi_du_lieu

# --- Các hàm xử lý giao diện ---
def them_moi_sinh_vien(danh_sach_sv, hien_thong_bao, root):
    def gui_them_moi_sv():
        nonlocal root
        ma_sv = entry_ma_sv.get()
        ho_ten = entry_ho_ten.get()
        gioi_tinh = entry_gioi_tinh.get()
        ngay_sinh_str = entry_ngay_sinh.get()
        try:
            ngay_sinh = datetime.datetime.strptime(
                ngay_sinh_str, "%d/%m/%Y"
            ).date()
            sv = SinhVien(ma_sv, ho_ten, gioi_tinh, ngay_sinh)
            if any(sv.ma_sv == item.ma_sv for item in danh_sach_sv):
                hien_thong_bao("Lỗi: Mã sinh viên đã tồn tại!")
            else:
                danh_sach_sv.append(sv)
                ghi_du_lieu("SV.bin", danh_sach_sv)
                hien_thong_bao("Đã thêm sinh viên!")
                clear_entry(window_them_sv)
                window_them_sv.destroy()
        except ValueError:
            hien_thong_bao("Lỗi: Ngày sinh không hợp lệ!")

    window_them_sv = tk.Toplevel(root)
    window_them_sv.title("Thêm mới sinh viên")
    window_them_sv.geometry("400x250")
    window_them_sv.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_them_sv, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=0, column=1, padx=5, pady=5)

    label_ho_ten = tk.Label(input_frame, text="Họ và tên:", font=("Arial", 12))
    label_ho_ten.grid(row=1, column=0, padx=5, pady=5)
    entry_ho_ten = tk.Entry(input_frame, font=("Arial", 12))
    entry_ho_ten.grid(row=1, column=1, padx=5, pady=5)

    label_gioi_tinh = tk.Label(input_frame, text="Giới tính:", font=("Arial", 12))
    label_gioi_tinh.grid(row=2, column=0, padx=5, pady=5)
    entry_gioi_tinh = tk.Entry(input_frame, font=("Arial", 12))
    entry_gioi_tinh.grid(row=2, column=1, padx=5, pady=5)

    label_ngay_sinh = tk.Label(input_frame, text="Ngày sinh (dd/mm/yyyy):", font=("Arial", 12))
    label_ngay_sinh.grid(row=3, column=0, padx=5, pady=5)
    entry_ngay_sinh = tk.Entry(input_frame, font=("Arial", 12))
    entry_ngay_sinh.grid(row=3, column=1, padx=5, pady=5)

    # --- Tạo button Thêm ---
    button_them_sv = tk.Button(
        window_them_sv, text="Thêm", command=gui_them_moi_sv, font=("Arial", 12),
        bg="#00a36c",
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_them_sv.pack(pady=10)


def sua_sinh_vien(danh_sach_sv, hien_thong_bao, root):
    def gui_sua_sv():
        nonlocal root
        ma_sv = entry_ma_sv.get()
        for sv in danh_sach_sv:
            if sv.ma_sv == ma_sv:
                sv.ho_ten = entry_ho_ten.get()
                sv.gioi_tinh = entry_gioi_tinh.get()
                try:
                    sv.ngay_sinh = datetime.datetime.strptime(
                        entry_ngay_sinh.get(), "%d/%m/%Y"
                    ).date()
                    ghi_du_lieu("SV.bin", danh_sach_sv)
                    hien_thong_bao("Đã sửa thông tin sinh viên!")
                    window_sua_sv.destroy()
                    return
                except ValueError:
                    hien_thong_bao("Lỗi: Ngày sinh không hợp lệ!")
                    return
        hien_thong_bao("Lỗi: Không tìm thấy sinh viên!")

    window_sua_sv = tk.Toplevel(root)
    window_sua_sv.title("Sửa thông tin sinh viên")
    window_sua_sv.geometry("400x250")
    window_sua_sv.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_sua_sv, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=0, column=1, padx=5, pady=5)

    label_ho_ten = tk.Label(input_frame, text="Họ và tên:", font=("Arial", 12))
    label_ho_ten.grid(row=1, column=0, padx=5, pady=5)
    entry_ho_ten = tk.Entry(input_frame, font=("Arial", 12))
    entry_ho_ten.grid(row=1, column=1, padx=5, pady=5)

    label_gioi_tinh = tk.Label(input_frame, text="Giới tính:", font=("Arial", 12))
    label_gioi_tinh.grid(row=2, column=0, padx=5, pady=5)
    entry_gioi_tinh = tk.Entry(input_frame, font=("Arial", 12))
    entry_gioi_tinh.grid(row=2, column=1, padx=5, pady=5)

    label_ngay_sinh = tk.Label(input_frame, text="Ngày sinh (dd/mm/yyyy):", font=("Arial", 12))
    label_ngay_sinh.grid(row=3, column=0, padx=5, pady=5)
    entry_ngay_sinh = tk.Entry(input_frame, font=("Arial", 12))
    entry_ngay_sinh.grid(row=3, column=1, padx=5, pady=5)

    # --- Tạo button Sửa ---
    button_sua_sv = tk.Button(
        window_sua_sv, text="Sửa", command=gui_sua_sv, font=("Arial", 12),
        bg="#0078d7",  # Màu xanh dương
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_sv.pack(pady=10)


def xoa_sinh_vien(danh_sach_sv, hien_thong_bao, root):
    def gui_xoa_sv():
        nonlocal root
        ma_sv = entry_ma_sv.get()
        for sv in danh_sach_sv:
            if sv.ma_sv == ma_sv:
                danh_sach_sv.remove(sv)
                ghi_du_lieu("SV.bin", danh_sach_sv)
                hien_thong_bao("Đã xóa sinh viên!")
                window_xoa_sv.destroy()
                return
        hien_thong_bao("Lỗi: Không tìm thấy sinh viên!")

    window_xoa_sv = tk.Toplevel(root)
    window_xoa_sv.title("Xóa sinh viên")
    window_xoa_sv.geometry("300x150")
    window_xoa_sv.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_xoa_sv, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=0, column=1, padx=5, pady=5)

    # --- Tạo button Xóa ---
    button_xoa_sv = tk.Button(
        window_xoa_sv, text="Xóa", command=gui_xoa_sv, font=("Arial", 12),
        bg="#c42b1c",  # Màu đỏ
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_sv.pack(pady=10)


def them_moi_hoc_phan(danh_sach_hp, hien_thong_bao, root):
    def gui_them_moi_hp():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        ten_hp = entry_ten_hp.get()
        hp = HocPhan(ma_hp, ten_hp)
        if any(hp.ma_hp == item.ma_hp for item in danh_sach_hp):
            hien_thong_bao("Lỗi: Mã học phần đã tồn tại!")
        else:
            danh_sach_hp.append(hp)
            ghi_du_lieu("HP.bin", danh_sach_hp)
            hien_thong_bao("Đã thêm học phần!")
            clear_entry(window_them_hp)
            window_them_hp.destroy()

    window_them_hp = tk.Toplevel(root)
    window_them_hp.title("Thêm mới học phần")
    window_them_hp.geometry("350x150")
    window_them_hp.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_them_hp, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    label_ten_hp = tk.Label(input_frame, text="Tên HP:", font=("Arial", 12))
    label_ten_hp.grid(row=1, column=0, padx=5, pady=5)
    entry_ten_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ten_hp.grid(row=1, column=1, padx=5, pady=5)

    # --- Tạo button Thêm ---
    button_them_hp = tk.Button(
        window_them_hp, text="Thêm", command=gui_them_moi_hp, font=("Arial", 12),
        bg="#00a36c",  # Màu xanh lá cây
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_them_hp.pack(pady=10)


def sua_hoc_phan(danh_sach_hp, hien_thong_bao, root):
    def gui_sua_hp():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        for hp in danh_sach_hp:
            if hp.ma_hp == ma_hp:
                hp.ten_hp = entry_ten_hp.get()
                ghi_du_lieu("HP.bin", danh_sach_hp)
                hien_thong_bao("Đã sửa thông tin học phần!")
                window_sua_hp.destroy()
                return
        hien_thong_bao("Lỗi: Không tìm thấy học phần!")

    window_sua_hp = tk.Toplevel(root)
    window_sua_hp.title("Sửa thông tin học phần")
    window_sua_hp.geometry("350x150")
    window_sua_hp.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_sua_hp, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    label_ten_hp = tk.Label(input_frame, text="Tên HP:", font=("Arial", 12))
    label_ten_hp.grid(row=1, column=0, padx=5, pady=5)
    entry_ten_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ten_hp.grid(row=1, column=1, padx=5, pady=5)

    # --- Tạo button Sửa ---
    button_sua_hp = tk.Button(
        window_sua_hp, text="Sửa", command=gui_sua_hp, font=("Arial", 12),
        bg="#0078d7",  # Màu xanh dương
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_hp.pack(pady=10)


def xoa_hoc_phan(danh_sach_hp, hien_thong_bao, root):
    def gui_xoa_hp():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        for hp in danh_sach_hp:
            if hp.ma_hp == ma_hp:
                danh_sach_hp.remove(hp)
                ghi_du_lieu("HP.bin", danh_sach_hp)
                hien_thong_bao("Đã xóa học phần!")
                window_xoa_hp.destroy()
                return
        hien_thong_bao("Lỗi: Không tìm thấy học phần!")

    window_xoa_hp = tk.Toplevel(root)
    window_xoa_hp.title("Xóa học phần")
    window_xoa_hp.geometry("300x150")
    window_xoa_hp.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_xoa_hp, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    # --- Tạo button Xóa ---
    button_xoa_hp = tk.Button(
        window_xoa_hp, text="Xóa", command=gui_xoa_hp, font=("Arial", 12),
        bg="#c42b1c",  # Màu đỏ
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_hp.pack(pady=10)


def them_moi_diem(danh_sach_diem, danh_sach_sv, danh_sach_hp, hien_thong_bao, root):
    def gui_them_moi_diem():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        ma_sv = entry_ma_sv.get()
        try:
            diem_so = float(entry_diem.get())
            sv = next((item for item in danh_sach_sv if item.ma_sv == ma_sv), None)
            hp = next((item for item in danh_sach_hp if item.ma_hp == ma_hp), None)

            if sv is None:
                hien_thong_bao("Lỗi: Không tìm thấy sinh viên!")
                return
            if hp is None:
                hien_thong_bao("Lỗi: Không tìm thấy học phần!")
                return

            diem_moi = Diem(ma_hp, ma_sv, diem_so)
            if any(
                diem_moi.ma_hp == item.ma_hp
                and diem_moi.ma_sv == item.ma_sv
                for item in danh_sach_diem
            ):
                hien_thong_bao("Lỗi: Bản ghi điểm đã tồn tại!")
            else:
                danh_sach_diem.append(diem_moi)
                ghi_du_lieu("Diem.bin", danh_sach_diem)
                hien_thong_bao("Đã thêm điểm!")
                clear_entry(window_them_diem)
                window_them_diem.destroy()
        except ValueError:
            hien_thong_bao("Lỗi: Điểm không hợp lệ!")

    window_them_diem = tk.Toplevel(root)
    window_them_diem.title("Thêm mới điểm")
    window_them_diem.geometry("350x200")
    window_them_diem.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_them_diem, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=1, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=1, column=1, padx=5, pady=5)

    label_diem = tk.Label(input_frame, text="Điểm:", font=("Arial", 12))
    label_diem.grid(row=2, column=0, padx=5, pady=5)
    entry_diem = tk.Entry(input_frame, font=("Arial", 12))
    entry_diem.grid(row=2, column=1, padx=5, pady=5)

    # --- Tạo button Thêm ---
    button_them_diem = tk.Button(
        window_them_diem, text="Thêm", command=gui_them_moi_diem, font=("Arial", 12),
        bg="#00a36c",  # Màu xanh lá cây
        fg="white",
        activebackground="#008a59",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_them_diem.pack(pady=10)

def sua_diem(danh_sach_diem, hien_thong_bao, root):
    def gui_sua_diem():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        ma_sv = entry_ma_sv.get()
        for diem in danh_sach_diem:
            if diem.ma_hp == ma_hp and diem.ma_sv == ma_sv:
                try:
                    diem.diem = float(entry_diem.get())
                    ghi_du_lieu("Diem.bin", danh_sach_diem)
                    hien_thong_bao("Đã sửa điểm!")
                    window_sua_diem.destroy()
                    return
                except ValueError:
                    hien_thong_bao("Lỗi: Điểm không hợp lệ!")
                    return
        hien_thong_bao("Lỗi: Không tìm thấy bản ghi!")

    window_sua_diem = tk.Toplevel(root)
    window_sua_diem.title("Sửa điểm")
    window_sua_diem.geometry("350x200")
    window_sua_diem.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_sua_diem, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=1, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=1, column=1, padx=5, pady=5)

    label_diem = tk.Label(input_frame, text="Điểm:", font=("Arial", 12))
    label_diem.grid(row=2, column=0, padx=5, pady=5)
    entry_diem = tk.Entry(input_frame, font=("Arial", 12))
    entry_diem.grid(row=2, column=1, padx=5, pady=5)

    # --- Tạo button Sửa ---
    button_sua_diem = tk.Button(
        window_sua_diem, text="Sửa", command=gui_sua_diem, font=("Arial", 12),
        bg="#0078d7",  # Màu xanh dương
        fg="white",
        activebackground="#0063b1",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_sua_diem.pack(pady=10)


def xoa_diem(danh_sach_diem, hien_thong_bao, root):
    def gui_xoa_diem():
        nonlocal root
        ma_hp = entry_ma_hp.get()
        ma_sv = entry_ma_sv.get()
        for diem in danh_sach_diem:
            if diem.ma_hp == ma_hp and diem.ma_sv == ma_sv:
                danh_sach_diem.remove(diem)
                ghi_du_lieu("Diem.bin", danh_sach_diem)
                hien_thong_bao("Đã xóa điểm!")
                window_xoa_diem.destroy()
                return
        hien_thong_bao("Lỗi: Không tìm thấy bản ghi!")

    window_xoa_diem = tk.Toplevel(root)
    window_xoa_diem.title("Xóa điểm")
    window_xoa_diem.geometry("300x150")
    window_xoa_diem.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_xoa_diem, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_hp = tk.Label(input_frame, text="Mã HP:", font=("Arial", 12))
    label_ma_hp.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_hp = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_hp.grid(row=0, column=1, padx=5, pady=5)

    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=1, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=1, column=1, padx=5, pady=5)

    # --- Tạo button Xóa ---
    button_xoa_diem = tk.Button(
        window_xoa_diem, text="Xóa", command=gui_xoa_diem, font=("Arial", 12),
        bg="#c42b1c",  # Màu đỏ
        fg="white",
        activebackground="#9f2317",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_xoa_diem.pack(pady=10)


def in_bang_diem(danh_sach_diem, danh_sach_sv, danh_sach_hp, hien_thong_bao, root):
    def gui_in_bang_diem():
        nonlocal root
        ma_sv = entry_ma_sv.get()
        sv = next(
            (item for item in danh_sach_sv if item.ma_sv == ma_sv), None
        )
        if sv is None:
            hien_thong_bao("Lỗi: Không tìm thấy sinh viên!")
            return

        # Tạo một cửa sổ mới để hiển thị bảng điểm
        window_bang_diem = tk.Toplevel(root)
        window_bang_diem.title(f"Bảng điểm sinh viên: {sv.ho_ten}")

        # Tạo Treeview để hiển thị dữ liệu
        tree = ttk.Treeview(
            window_bang_diem,
            columns=("Mã HP", "Tên HP", "Điểm"),
            show="headings",
        )
        tree.heading("Mã HP", text="Mã HP")
        tree.heading("Tên HP", text="Tên HP")
        tree.heading("Điểm", text="Điểm")
        tree.pack(fill="both", expand=True)

        # Thêm dữ liệu vào Treeview
        for diem in danh_sach_diem:
            if diem.ma_sv == ma_sv:
                hp = next(
                    (
                        item
                        for item in danh_sach_hp
                        if item.ma_hp == diem.ma_hp
                    ),
                    None,
                )
                if hp:
                    tree.insert(
                        "",
                        "end",
                        values=(hp.ma_hp, hp.ten_hp, diem.diem),
                    )

    window_in_diem = tk.Toplevel(root)
    window_in_diem.title("In bảng điểm")
    window_in_diem.geometry("300x150")
    window_in_diem.resizable(False, False)

    # --- Tạo frame cho các label và entry ---
    input_frame = tk.Frame(window_in_diem, bg="#f0f0f0")
    input_frame.pack(pady=10)

    # --- Tạo các label và entry ---
    label_ma_sv = tk.Label(input_frame, text="Mã SV:", font=("Arial", 12))
    label_ma_sv.grid(row=0, column=0, padx=5, pady=5)
    entry_ma_sv = tk.Entry(input_frame, font=("Arial", 12))
    entry_ma_sv.grid(row=0, column=1, padx=5, pady=5)

    # --- Tạo button In ---
    button_in_diem = tk.Button(
        window_in_diem, text="In", command=gui_in_bang_diem, font=("Arial", 12),
        bg="#2b88d8",  # Màu xanh dương
        fg="white",
        activebackground="#2060a5",
        activeforeground="white",
        padx=10,
        pady=5,
    )
    button_in_diem.pack(pady=10)


def clear_entry(window):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, "end")