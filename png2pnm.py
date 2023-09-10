from PIL import Image

def png2pnm(
    PNG檔案目錄="./clipped_png",
    檔案編號起始=1,
    檔案編號結束=10,
    PNM檔案目錄="./clipped_pnm"
):
    for i in range(檔案編號起始, 檔案編號結束+1):
        print("\n---------------")
        print(f"處理編號為 {i} 的檔案…")
        image = Image.open(f"{PNG檔案目錄}/{i}.png")
        image.save(f"{PNM檔案目錄}/{i}.pnm")        
        print("存檔完畢")
