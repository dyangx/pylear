import base64
from contextlib import closing
from os import rename
from time import sleep

import requests
from filetype import guess


class File:
    @staticmethod
    def openFile(self):
        with open("../file/data.txt", 'r', encoding='utf-8') as f:
            for line in f.readlines():
                print(line)

    @staticmethod
    def openFile1(self):
        with open("../file/data.txt", 'a', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print(line),  # 加了 ',' 是为了避免 print 自动换行

                f.write("if you ....")

    @staticmethod
    def img():
        with open("../file/无标题流程图.drawio.png", "rb") as f:
            data = f.read()
            print(data)
            base64_data = base64.b64encode(data)
            print(base64_data)

    @staticmethod
    def download_file():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        file_full_name = "../file/hh"
        file_url = "https://pic.rmb.bdstatic.com/1530971282b420d77bdfb6444d854f952fe31f0d1e.jpeg"
        # 开始下载图片
        i = 0
        with closing(requests.get(file_url, headers=headers, stream=True)) as response:
            chunk_size = 1  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 文件总大小 ████
            data_count = 0  # 当前已传输的大小
            print("正在下载中。。。。。。。。。。")
            with open(file_full_name, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    done_block = int((data_count / content_size) * 50)
                    data_count = data_count + len(data)
                    now_jd = (data_count / content_size) * 100
                    print("\r %s：[%s%s] %.2lf%%" % (
                    file_full_name, done_block * '█', ' ' * (50 - 1 - done_block), now_jd), end=" ")
                    # sleep(1)
        # 下载完图片后获取图片扩展名，并为其增加扩展名
        file_type = guess(file_full_name)
        rename(file_full_name, file_full_name + '.' + file_type.extension)
        print("\r下载完成。。。。。。。。。。")


if __name__ == '__main__':
    File.download_file()

