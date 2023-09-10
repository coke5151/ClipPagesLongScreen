from pikepdf import Pdf
def split_pdf(要分割的單檔多頁PDF檔 = "./pdf_unsplit/example.pdf", 輸出檔案的編碼從幾開始 = 1, 存檔目錄 = "./pdf_splitted"):
    pdf = Pdf.open(要分割的單檔多頁PDF檔)
    pages = pdf.pages
    output = Pdf.new()
    i = 輸出檔案的編碼從幾開始
    for page in pages:
        output = Pdf.new()
        output.pages.append(page)
        output.save(f"{存檔目錄}/splitted_{i}.pdf")
        i += 1

