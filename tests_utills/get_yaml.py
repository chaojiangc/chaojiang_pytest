import yaml

'''
获得yaml数据
'''

'''正确学生账号'''
def get_yaml_stur():
    file1 = open('D:\pytest\pytest_0613\\tests_data\\stu_loginR.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2


'''正确学生账号,错误密码'''
def get_yaml_stuf():
    file1 = open('D:\pytest\pytest_0613\\tests_data\stu_loginF.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2


'''正确学生账号，密码为空'''
def get_yaml_stuf1():

    file1 = open('D:\pytest\pytest_0613\\tests_data\stu_loginF2.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2

'''学生账号空，密码为空'''
def get_yaml_stuf2():

    file1 = open('D:\pytest\pytest_0613\\tests_data\stu_loginF3.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2

'''正确老师账号'''
def get_yaml_tear():
    file1 = open('D:\pytest\pytest_0613\\tests_data\\tea_loginR.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2

'''正确老师账号,错误密码'''
def get_yaml_tear1():
    file1 = open('D:\pytest\pytest_0613\\tests_data\\tea_loginF.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2

'''正确老师账号,错误空'''
def get_yaml_tear2():
    file1 = open('D:\pytest\pytest_0613\\tests_data\\tea_loginF2.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2

'''正确老师账号,错误空'''
def get_yaml_tear3():
    file1 = open('D:\pytest\pytest_0613\\tests_data\\tea_loginF3.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2