import base64


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
