"""
@Author:chengchao
"""

import pytest,allure
from tests_utills.get_yaml import get_yaml_stuf2
from songshu_code.songshuai_api import amg


@allure.feature("线下客户端登录业务")
@allure.story("学生账号为空，密码为空登录")
@allure.title("登录失败")
@pytest.mark.parametrize("datas", get_yaml_stuf2())
def test_login(datas):
    with allure.step('获得签名sign'):
        sig = amg.get_sign(datas['username'], datas['pwd'], datas['productkey'])
        sgi1 = str(sig)

    with allure.step('学生账号登录'):
        url_fomal = "https://client.songshuai.com/api/login"
        responses = amg.login_stu(url_fomal, datas['username'], datas['pwd'], sig=sgi1)
        res = responses.json()
        assert res['msg'] == datas['expectedmsg']



if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_stulogin4.py"])