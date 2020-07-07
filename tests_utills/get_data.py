#D:\pytest\pytest_0613\tests\client_songshuai\test_stulogin1.py
#D:\pytest\pytest_0613\tests_data

import os


def get_data_path(case_path):
    file_name = os.path.dirname(case_path).split(os.sep+"tests"+os.sep)
    print(file_name)


if __name__ == '__main__':
   get_data_path("D:\pytest\pytest_0613\\tests\client_songshuai\\test_stulogin1.py")
