# -*- coding: utf-8 -*-
# author: hiro
import os


def rename_file():
    #(1) get file names from the floder
    # floder_path = r"C:\Users\Administrator\Desktop\Udacity\p2\prank"
    floder_path = r"C:\Users\Administrator\Desktop\Udacity\p2\alphabet\new"
    file_list = os.listdir(floder_path)
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(floder_path)
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_file()