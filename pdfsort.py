import os
def left_right_pdfsort(
    編號 = range(1, 1451, 2),
    PDF檔案目錄 = "."
):
    for i in 編號:
        os.rename(f"{PDF檔案目錄}/splitted_{i}.pdf", f"{PDF檔案目錄}/splitted_{i+1}TEMP.pdf")
        os.rename(f"{PDF檔案目錄}/splitted_{i+1}.pdf", f"{PDF檔案目錄}/splitted_{i}.pdf")
        os.rename(f"{PDF檔案目錄}/splitted_{i+1}TEMP.pdf", f"{PDF檔案目錄}/splitted_{i+1}.pdf")