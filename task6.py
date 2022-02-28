#погружение в python
#неделя 3 задание 1
#класс для чтения из файла

class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path) as f:
                return f.read()
        except IOError:
            return ""