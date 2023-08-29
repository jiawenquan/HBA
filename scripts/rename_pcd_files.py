import os

# 指定文件夹路径
folder_path = "/GOSLAM/Downloads/GOSLAM/2023-08-17-22-53-37/pcd/"

# 列出所有.pcd文件
files = [f for f in os.listdir(folder_path) if f.endswith('.pcd')]

# 对于每个文件
for file in files:
    # 提取文件名的数字部分，不包括扩展名
    number = file.rstrip('.pcd')

    # 使用zfill方法填充前导零
    new_number = number.zfill(5)

    # 生成新的文件名
    new_filename = f'{new_number}.pcd'

    # 获取旧文件和新文件的完整路径
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_filename)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

print("文件重命名完成！")
