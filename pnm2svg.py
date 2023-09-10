import os
def pnm2svg(
    PNM絕對目錄 = "C:\\repos\\clip-pages-long_screen\\clipped_pnm",
    檔案編碼開始 = 1,
    檔案編碼結束 = 10,
    SVG絕對目錄 = "C:\\repos\\clip-pages-long_screen\\clipped_svg",
    WINDOWS系統路徑為反斜線 = True
):
    curr_path = os.getcwd()
    print(curr_path)
    if(WINDOWS系統路徑為反斜線):
        for i in range(檔案編碼開始, 檔案編碼結束+1):
            print("\n---------------------")
            print(f"處理編號為 {i} 的檔案…")
            os.system(f"potrace {PNM絕對目錄}\\{i}.pnm --svg -o {SVG絕對目錄}\\{i}.svg")        
            print("存檔完畢")
    else:
        for i in range(檔案編碼開始, 檔案編碼結束+1):
            print("\n---------------------")
            print(f"處理編號為 {i} 的檔案…")            
            os.system(f"potrace {PNM絕對目錄}/{i}.pnm --svg -o {SVG絕對目錄}/{i}.svg")