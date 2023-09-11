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

def split_pdf_bypage(要分割的單檔多頁PDF檔 = "./principles_of_physics_12e.pdf",
                    每多少頁要分割一檔 = 300,
                    存檔目錄 = "."):
    pdf = Pdf.open(要分割的單檔多頁PDF檔)
    pages = pdf.pages
    
    p = 0
    i = 1
    
    for page in pages:
        print(f"處理第 {p+1} 頁…")
        if(p % 每多少頁要分割一檔 == 0):
            if p == 0:
                output = Pdf.new()
                output.pages.append(page)
            else:
                print(f"已達 {每多少頁要分割一檔} 頁，分割存檔…")
                output.save(f"{存檔目錄}/part_{i}.pdf")
                print("存檔完畢")
                i += 1
                output = Pdf.new()
                output.pages.append(page)
        else:
            if len(pages) - (p+1) == 0:
                output.pages.append(page)
                print(f"最後一份，切不滿 {每多少頁要分割一檔} 頁，分割存檔…")
                output.save(f"{存檔目錄}/part_{i}.pdf")
                print("存檔完畢")
            else:
                output.pages.append(page)
        p += 1