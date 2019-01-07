'''
最终目标是进入每一个目录，把MP3文件copy到同一个目录中

'''

import os
import shutil


def copy_mp3(file_dir, new_path):
    '''
    将目标目录及其子目录下的所有MP3文件 复制到新的路径中
    args:
            file_dir: 初始根目录
            new_path: 目标目录
    '''
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for file in filenames:
            if os.path.splitext(file)[1] == '.mp3':
                file_path = os.path.join(dirpath, file)
                des_path = os.path.join(new_path, file)
                print(file)
                shutil.copy(file_path, des_path)


root_path = "D:\迅雷下载\薛兆丰的北大经济学课"
d_path = "D:\\xzf_economics"
copy_mp3(root_path, d_path)
