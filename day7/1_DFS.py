import os
import sys


def scan_dir(current_path,width):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path) #得到当前文件夹下所有文件
    for file in file_list:
        print(' '*width,file) #打印文件名,width代表多少个空格缩进
        new_path = current_path + '/' + file #路径拼接
        if os.path.isdir(new_path):
            scan_dir(new_path,width + 4)


if __name__ == '__main__':
    scan_dir('C:\\Users\\Antenna\\Desktop\\wdPython25',0)
    print(sys.argv)