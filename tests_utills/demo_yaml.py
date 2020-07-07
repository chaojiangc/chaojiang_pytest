import yaml,pytest,allure
from songshu_code.songshuai_api import amg



def get_yaml_data1():
    file1 = open('stu_loginR.yaml', 'r', encoding='utf-8')
    file2 = yaml.full_load(file1)
    file1.close()
    return file2


@allure.feature("线下客户端登录业务")
@allure.story("学生账号正确，密码正确登录")
@allure.title("登录成功")
# @allure.step
@pytest.mark.parametrize("datas", get_yaml_data1())
@allure.description('我来这里测试description')
def test_login(datas):
    allure.dynamic.description("------test--------")

    with allure.step('获得签名'):
        sig = amg.get_sign(datas['username'],datas['pwd'])
        sig1 = str(sig)

    allure.attach('用例参数', datas['username'],datas['pwd'])
    with allure.step('请求登录api'):
        url_fomal = "https://client.songshuai.com/api/stulogin"
        responses = amg.login_stu(url_fomal, datas['username'], datas['pwd'], sig=sig1)
        res = responses.json()
        assert res['msg'] == datas['msg']


if __name__ == '__main__':
    pytest.main(["-s", "-v", "demo_yaml.py"])







