

import shutil
import os

def copy_folder(source_folder, destination_folder):
    try:
        # 复制文件夹
        shutil.copytree(source_folder, destination_folder)
        print(f"成功复制文件夹：{source_folder} 到 {destination_folder}")
    except Exception as e:
        print(f"复制文件夹时出错：{e}")

# 示例使用
source = "/data2/hejt/yolov9/dataset/images/train"  # 替换为源文件夹路径
destination = "/data2/hejt/yolov11/ultralytics-main/ultralytics/datasets/images" # 替换为目标文件夹路径

copy_folder(source, destination)



import shutil
import os

def copy_files(source_folder, destination_folder):
    try:
        # 确保目标文件夹存在，如果不存在则创建
        os.makedirs(destination_folder, exist_ok=True)

        # 遍历源文件夹中的所有文件
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            
            # 复制文件
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"成功复制文件：{source_file} 到 {destination_file}")
            else:
                print(f"跳过非文件项：{source_file}")

    except Exception as e:
        print(f"复制文件时出错：{e}")

# 示例使用
source = "/data2/hejt/yolov9/dataset/labels/test"  # 替换为源文件夹路径
destination = "/data2/hejt/yolov11/ultralytics-main/ultralytics/datasets/labels/test"

copy_files(source, destination)

