# 使用本程式的環境：
# 1：安裝好 Python 3（我開發時用的是 Python 3.11.5）
# 2：pip install -r requirements.txt
# 3：自行安裝好 poppler
# 4：自行安裝好 potrace
# 5：自行安裝好在你系統中 cairosvg 需要的依賴項

# 本程式的功能：
# split_pdf：將給予的長篇多頁 PDF 檔（例如 Fireshot 截圖後存的 PDF 檔案（有分頁））分割
# split_pdf_bypage：將給予的長篇多頁 PDF 檔以指定的頁數分割
# pdf2png：將整個資料夾中的 PDF 檔案依次轉換為 PNG 檔案
# manual_clip：對指定的檔案進行裁切（依照像素座標）（像素座標可在小畫家中查詢）
# AUTO CLIP：對指定目錄下的多個檔案進行裁切（依照像素座標）
# pngs2pdf：將裁切好的多個 PNG 檔轉換為一個 PDF 檔（多頁）
# merge_pdf：進行 PDF 合併

from split_pdf import split_pdf, split_pdf_bypage
from manualclip import manualclip
from pdf2png import pdf2png
from png2pdf import pngs2pdf
from merge_pdf import merge_pdf
######### Functions，可解除註解後直接執行本檔案（main.py）使用 #########
#---------------------------------------------------------------------
# split_pdf(要分割的單檔多頁PDF檔 = "C:\\Users\\User\\Desktop\\ebooks\\part_5.pdf",
#           輸出檔案的編碼從幾開始 = 1201,
#           存檔目錄 = "C:\\Users\\User\\Desktop\\ebooks\\pdf_splitted")

#---------------------------------------------------------------------
pdf2png(PDF目錄="/content/drive/My Drive/書籍資料/principles of physics 12e",
        編號開始=1,
        編號結束=5,
        PNG存檔目錄="/content/drive/My Drive/書籍資料/principles of physics 12e/splitted_png",
        DPI = 100)

#---------------------------------------------------------------------
# manualclip(
#     左上角x座標 = 144,
#     左上角y座標 = 591,
#     右下角x座標 = 7695,
#     右下角y座標 = 10243,
#     亮度 = 1,
#     對比 = 1,
#     飽和度 = 1,
#     銳利度 = 1,
#     來源圖片目錄 = "E:\\manual_clip\\863.png",
#     存檔目錄名稱 = "E:\clipped_png\\863.png",
# )

#--------------------AUTO CLIP----------------------------------------
# Note: 缺 1、2、862、863
# 原始檔目錄 = "E:\\unclipped_png"
# 存檔目錄 = "E:\\clipped_png"
# 編號起始 = 103
# 編號結束 = 861
# for i in range(編號起始, 編號結束+1):
#     print(f"\n---------------------\n處理編號 {i} 的檔案…")
#     manualclip(
#         左上角x座標 = 144,
#         左上角y座標 = 10,
#         右下角x座標 = 7692,
#         右下角y座標 = 9657,
#         亮度 = 1,
#         對比 = 1,
#         飽和度 = 1,
#         銳利度 = 1,
#         來源圖片目錄 = f"{原始檔目錄}\\{i}.png",
#         存檔目錄名稱 = f"{存檔目錄}\\{i}.png",
#     )

#---------------------------------------------------------------------
# pngs2pdf(
#         圖片目錄 = "E:\\clipped_png",
#         圖片編號開始 = 1451,
#         圖片編號結束 = 1457,
#         PDF存檔目錄檔名 = f"./result_1451.pdf"
# )

#---------------------------------------------------------------------
# merge_pdf(
#     編號 = range(1, 1461, 10),
#     PDF檔案目錄 = ".",
#     合併檔案存檔 = "./final_result.pdf"
# )

#---------------------------------------------------------------------
# split_pdf_bypage(要分割的單檔多頁PDF檔 = "./principles_of_physics_12e.pdf",
#                     每多少頁要分割一檔 = 300,
#                     存檔目錄 = ".")