from pikepdf import Pdf
def merge_pdf(
    編號 = range(1, 1451, 10),
    PDF檔案目錄 = ".",
    合併檔案存檔 = "./final_result.pdf"
):
    output = Pdf.new()     
    for i in 編號:
        print(f"合併第 {i} 編號的檔案…")
        pdf = Pdf.open(f"{PDF檔案目錄}/result_{i}.pdf")
        output.pages.extend(pdf.pages)
    print("存檔…")
    output.save(合併檔案存檔)
    print("存檔完畢")