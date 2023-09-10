# 使用本程式的環境：
# 1：安裝好 Python 3（我開發時用的是 Python 3.11.5）
# 2：pip install requirements.txt
# 3：自行安裝好 poppler
# 4：自行安裝好 potrace
# 5：自行安裝好在你系統中 cairosvg 需要的依賴項

# 本程式的功能：
# split_pdf：將給予的長篇多頁 PDF 檔（例如 Fireshot 截圖後存的 PDF 檔案（有分頁））分割
# pdf2png：將整個資料夾中的 PDF 檔案依次轉換為 PNG 檔案
# manual_clip：對指定的檔案進行裁切（依照像素座標）（像素座標可在小畫家中查詢）
# AUTO CLIP：對指定目錄下的多個檔案進行裁切（依照像素座標）
# png2pdf：將裁切好的多個 PNG 檔轉換為一個 PDF 檔（多頁）
# png2pnm：將裁切好的 PNG 檔轉換為 PNM
# pnm2svg：利用 Potrace 將 PNG 轉換為 SVG 向量檔
# SVG 合成為單一 PDF 檔（多頁）

from split_pdf import split_pdf
from manualclip import manualclip
from pdf2png import pdf2png
from png2pnm import png2pnm
from pnm2svg import pnm2svg
######### Functions，可解除註解後直接執行本檔案（main.py）使用 #########
#---------------------------------------------------------------------
# split_pdf(要分割的單檔多頁PDF檔 = "./pdf_unsplit/cover~867.pdf",
#           輸出檔案的編碼從幾開始 = 1,
#           存檔目錄 = "./pdf_splitted")

#---------------------------------------------------------------------
# pdf2png(PDF目錄="./pdf_splitted",
#         編號開始=1,
#         編號結束=1457,
#         PNG存檔目錄="./unclipped_png")

#---------------------------------------------------------------------
# manualclip(
#     左上角x座標 = 144,
#     左上角y座標 = 392,
#     右下角x座標 = 7692,
#     右下角y座標 = 10039,
#     亮度 = 1,
#     對比 = 1,
#     飽和度 = 1,
#     銳利度 = 1,
#     來源圖片目錄 = "./manual_clip/example.png",
#     存檔目錄名稱 = "./clipped_png/example.png",
# )

#--------------------AUTO CLIP----------------------------------------
# 原始檔目錄 = "./unclipped_png"
# 存檔目錄 = "./clipped_png"
# 編號起始 = 3
# 編號結束 = 472
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
#         來源圖片目錄 = f"{原始檔目錄}/{i}.png",
#         存檔目錄名稱 = f"{存檔目錄}/{i}.png",
#     )

#---------------------------------------------------------------------
# png2pnm(
#     PNG檔案目錄="./clipped_png",
#     檔案編號起始=1,
#     檔案編號結束=10,
#     PNM檔案目錄="./clipped_pnm"
# )

#---------------------------------------------------------------------
# pnm2svg( # 這個函數只能用絕對目錄
#     PNM絕對目錄 = "C:\\repos\\clip-pages-long_screen\\clipped_pnm",
#     檔案編碼開始 = 1,
#     檔案編碼結束 = 10,
#     SVG絕對目錄 = "C:\\repos\\clip-pages-long_screen\\clipped_svg",
#     WINDOWS系統路徑為反斜線 = True
# )