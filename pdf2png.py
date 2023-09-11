import os
from PIL import Image, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
from pdf2image import convert_from_path

def pdf2png(PDF目錄="./pdf_splitted/part1", 編號開始=1, 編號結束=1400, PNG存檔目錄="./unclipped_png", DPI=200):
    i = 1
    for n in range(編號開始, 編號結束+1): # range 為左閉右開
        filename = f"{PDF目錄}/splitted_{n}.pdf"
        pages = convert_from_path(filename, DPI)
        for page in pages:
            print("\n-----------------")
            print(f"處理第 {i} 張…")
            print(filename)
            page.save(f"{PNG存檔目錄}/{n}.png", "png")
            print("存檔完畢")
            i += 1