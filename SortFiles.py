import os
import shutil
from pathlib import Path

def organize_files(target_directory):
    """
    根據副檔名自動分類檔案並移動到新資料夾中。
    """
    # 將路徑轉換為 Path 物件
    base_path = Path(target_directory)
    
    if not base_path.exists():
        print(f"錯誤：路徑 '{target_directory}' 不存在。")
        return

    print(f"正在整理資料夾：{base_path.absolute()}")

    for item in base_path.iterdir():
        # 跳過資料夾，只處理檔案
        if item.is_dir():
            continue
        
        # 跳過腳本自身（避免移動正在執行的程式碼）
        if item.name == Path(__file__).name:
            continue

        # 取得副檔名（去掉點號並轉為大寫，方便統一名稱）
        # 如果沒有副檔名，則分類到 'Others'
        extension = item.suffix.lower().replace('.', '')
        if not extension:
            extension = "no_extension"

        dest_folder = base_path / extension
        
        # 如果資料夾不存在則建立
        if not dest_folder.exists():
            try:
                dest_folder.mkdir()
                print(f"建立新資料夾：[{extension}]")
            except Exception as e:
                print(f"無法建立資料夾 {extension}: {e}")
                continue

        try:
            # 處理檔名衝突：如果目標資料夾已有同名檔案，則不覆蓋
            dest_path = dest_folder / item.name
            if dest_path.exists():
                print(f"注意：檔案 '{item.name}' 已存在於 '{extension}' 中，已跳過。")
            else:
                shutil.move(str(item), str(dest_path))
                print(f"已移動：{item.name} -> [{extension}]")
        except Exception as e:
            print(f"移動檔案 {item.name} 時發生錯誤: {e}")

if __name__ == "__main__":
    # 您可以修改這裡的路徑，或是使用 "." 代表目前腳本所在的目錄
    target_dir = input("請輸入要整理的資料夾路徑 (直接按 Enter 整理當前目錄): ").strip()
    
    if not target_dir:
        target_dir = "."
        
    organize_files(target_dir)
    print("\n整理完成！")