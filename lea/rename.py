import os
from ctypes import WinError


def rename(base_path):
    for dir_path, dir_name, filenames in os.walk(base_path):
        if len(filenames) > 0:
            for file_name in filenames:
                if file_name.find("666java") > -1:
                    rename_file(dir_path+"\\"+file_name)


def rename_file(file_path):
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    if file_name.find("666java") > -1:
        start = file_name.find("【")
        end = file_name.rfind("】")
        str = file_name[start:end + 1]
        file_name = file_name.replace(str, "")
        new_path = file_dir + "\\" + file_name
        try:
            os.rename(file_path, new_path)
        except BaseException as e:
            print('Error:',e)
            pass
        print(new_path)


if __name__ == '__main__':
    rename('F:\\video')
