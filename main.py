from PIL import Image, ImageEnhance

############### 控制面版 ###############
亮度 = 0.9
對比 = 2
飽和度 = 1
銳利度 = 1
圖片目錄 = "1.jpg"
############### 控制面版 ###############


img = Image.open(圖片目錄)
print(img.size)
# img.show()
i = 1172
n = 1
bottom = img.size[1]
while( (i+1082) < bottom ):
    print("\n-----------------------------")
    print(f"處理第 {n} 張圖片：")
    new_img = img.crop((10, i, 864, i+1082))                    # (left, upper, right, lower)
    print("調整對比度…")
    contrast = ImageEnhance.Contrast(new_img)                   # 調整對比
    output_contrast = contrast.enhance(對比)                     # 提高對比

    print("調整亮度…")
    brightness = ImageEnhance.Brightness(output_contrast)       # 調整亮度
    output_brightness = brightness.enhance(亮度)                 # 提高亮度

    print("調整飽和度…")
    color = ImageEnhance.Color(output_brightness)               # 調整飽和度
    output_color = color.enhance(飽和度)                         # 提高飽和度

    print("調整銳利度…")
    sharpness = ImageEnhance.Sharpness(output_color)   # 調整銳利度
    output = sharpness.enhance(銳利度)        # 提高銳利度

    print("存檔…")
    output.save(f"./clipped/clipped_{n}.jpg")

    print("存檔完畢")
    i += 1103
    n += 1