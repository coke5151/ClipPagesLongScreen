from PIL import Image, ImageEnhance
Image.MAX_IMAGE_PIXELS = None

def manualclip(
    左上角x座標 = 1,
    左上角y座標 = 1,
    右下角x座標 = 500,
    右下角y座標 = 500,
    亮度 = 1,
    對比 = 1,
    飽和度 = 1,
    銳利度 = 1,
    來源圖片目錄 = "./manual_clip/example.png",
    存檔目錄名稱 = "./clipped_png/example.png",
):
    
    img = Image.open(來源圖片目錄)
    print(img.size)
    # img.show()

    print("調整對比度…")
    contrast = ImageEnhance.Contrast(img)                   # 調整對比
    output_contrast = contrast.enhance(對比)                     # 提高對比

    print("調整亮度…")
    brightness = ImageEnhance.Brightness(output_contrast)       # 調整亮度
    output_brightness = brightness.enhance(亮度)                 # 提高亮度

    print("調整飽和度…")
    color = ImageEnhance.Color(output_brightness)               # 調整飽和度
    output_color = color.enhance(飽和度)                         # 提高飽和度

    print("調整銳利度…")
    sharpness = ImageEnhance.Sharpness(output_color)   # 調整銳利度
    output_full = sharpness.enhance(銳利度)        # 提高銳利度

    new_img = output_full.crop((左上角x座標, 左上角y座標, 右下角x座標, 右下角y座標)) # (left, upper, right, lower)

    print("存檔…")
    new_img.save(存檔目錄名稱)

    print("存檔完畢")
