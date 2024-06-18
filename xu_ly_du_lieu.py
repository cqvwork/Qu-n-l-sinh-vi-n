# Name: Chử Quang Vinh  
# Student ID: 20227074
# Class: 150327
# Project: 05 - Chương trình quản lí sinh viên
# Date: 06/06/2024

import pickle

def doc_du_lieu(file_name):
    try:
        with open(file_name, "rb") as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return []


def ghi_du_lieu(file_name, data):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)