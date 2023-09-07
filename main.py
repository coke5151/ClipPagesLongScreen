from PIL import Image, ImageEnhance

############### 控制面版 ###############
第一張圖左上角x座標 = 0
第一張圖左上角y座標 = 2558
第一張圖右下角x座標 = 1347
第一張圖右下角y座標 = 4354
第二張圖左上角y座標 = 4372

亮度 = 1
對比 = 1.25
飽和度 = 3
銳利度 = 1

圖片目錄 = "2.png"
存檔從編號多少開始 = 1
############### 控制面版 ###############


img = Image.open(圖片目錄)
print(img.size)
# img.show()

i = 第一張圖左上角y座標
n = 存檔從編號多少開始
height = 第一張圖右下角y座標 - 第一張圖左上角y座標
delta = 第二張圖左上角y座標 - 第一張圖左上角y座標

bottom = img.size[1]
while( (i+height) < bottom ):
    print("\n-----------------------------")
    print(f"處理第 {n} 張圖片：")
    new_img = img.crop((第一張圖左上角x座標, i, 第一張圖右下角x座標, i+height))                    # (left, upper, right, lower)
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
    output.save(f"./clipped/clipped_{n}.png")

    print("存檔完畢")
    i += delta
    n += 1