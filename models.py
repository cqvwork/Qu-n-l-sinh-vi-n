# Name: Chử Quang Vinh  
# Student ID: 20227074
# Class: 150327
# Project: 05 - Chương trình quản lí sinh viên
# Date: 06/06/2024

import datetime

class SinhVien:
    def __init__(self, ma_sv, ho_ten, gioi_tinh, ngay_sinh):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh = ngay_sinh

    def __str__(self):
        return f"Mã SV: {self.ma_sv}, Họ tên: {self.ho_ten}, Giới tính: {self.gioi_tinh}, Ngày sinh: {self.ngay_sinh}"


class HocPhan:
    def __init__(self, ma_hp, ten_hp):
        self.ma_hp = ma_hp
        self.ten_hp = ten_hp

    def __str__(self):
        return f"Mã HP: {self.ma_hp}, Tên HP: {self.ten_hp}"


class Diem:
    def __init__(self, ma_hp, ma_sv, diem):
        self.ma_hp = ma_hp
        self.ma_sv = ma_sv
        self.diem = diem

    def __str__(self):
        return f"Mã HP: {self.ma_hp}, Mã SV: {self.ma_sv}, Điểm: {self.diem}"