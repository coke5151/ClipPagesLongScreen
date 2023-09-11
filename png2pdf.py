from PIL import Image

def pngs2pdf(
    圖片目錄 = "E:\\clipped_png",
    圖片編號開始 = 1,
    圖片編號結束 = 1400,
    PDF存檔目錄檔名 = "E:\\result.pdf"
):
    images = [
        Image.open(f"{圖片目錄}/{n}.png")
        for n in range(圖片編號開始, 圖片編號結束+1)
    ]

    pdf_path = PDF存檔目錄檔名

    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )