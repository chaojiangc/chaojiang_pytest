"""
@Author:chengchao
"""

import json

import requests
import hashlib


class AMG:

    # 打印Response

    def _printResponse(self, response):
        print("----开始打印http响应消息----")
        print('状态码:')
        print(response.status_code)

        print('响应headers:')
        for k, v in response.headers.items():
            print(f'{k}:{v}')

        print(response.text)
        print(response.content.decode("utf8"))
        obj = response.json()
        print(obj)
        # print(obj['msg'])
        #

        print('----http响应消息结束----')


     #登录签名
    def get_sign(self, username, password):

        data = {
                "uname": username,
                "password": password,

               }
        new_data = sorted(data.items())
        # print(new_data)
        list1 = []
        P_key ='ca6992149568ae593403ad12b0c480bc'
        for k, v in new_data:
            test = f"{k}{v}"
            list1.append(test)
        list1.append(P_key)
        # print(list1)
        list2 = "".join(list1)
        # print(list2)




        sha = hashlib.sha1(list2.encode('utf-8'))
        sha1 = sha.hexdigest()
        sha2 =sha1.upper()

        # print(sha2)
        return sha2


    #统计接口登录签名
    def get_sign_sta(self):
        data = {
            "content": {"data":[{"login_res":"登录成功","login_status":1,"login_type":1,"phone":15511898673,"real_name":"李泽森","uid":6860100839851950,"uname":"sn29994lizesen","cellid":"","session_id":"2020525145606365","ismobiledevice":"false","appkey":"aac9d32a0eed820769aa1f120e6796db","resolution":"1366*768","lac":"","network":"wire","deviceid":"","version":"2.1.14","modulename":"Administrator","time":"2020-05-25 14:56:06","useridentifier":15511898673,"lib_version":"5.0.0","havegravity":"true","platform":"win32","havewifi":"true","os_version":"6.1.7601","phonetype":"1","havebt":"false","wifimac":"","devicename":"PC-20190616JUMM","mccmnc":"","language":"zh","imsi":"ia32","salt":"8e565b17182b4b57863ee8d7d8847e77","osversion":"6.1.7601","account_id":"","school_id":"","school_name":""}]}
        }
        # new_data = sorted(data.items())
        # print(new_data)

        list1 = []
        P_key = 'ca6992149568ae593403ad12b0c480bc'
        for k, v in data.items():
            test = f"{k}{v}"
            print(k)
            print(v)
            list1.append(test)
        list1.append(P_key)
        list2 = "".join(list1)
        list3 = list2.replace('\'', '\" ')
        list4 = list3.replace(' ', '')
        print(list1)
        print(list2)
        print(type(list2))
        print(list3)
        print(list4)
        #
        sha = hashlib.sha1(list4.encode('utf-8'))
        sha1 = sha.hexdigest()
        sha2 = sha1.upper()
        #
        print(sha)
        print(sha1)
        print(sha2)
        return sha2
        # return list2


    #学生登录
    def login_stu(self, url,username, password, sig):
        self.s = requests.session()
        url_formal = url
        data = {
               "uname": username,
               "password": password,
               "sign": sig
              }
        response = self.s.post(url_formal, data=data)
        self._printResponse(response)
        return response

     #老师登录
    def login_tea(self,url, username, password, sig):
        self.s = requests.session()
        url_formal = url
        data = {
            "uname": username,
            "password": password,
            "sign": sig
        }
        response = self.s.post(url_formal, data=data)
        self._printResponse(response)
        return response


      #统计接口登录
    def login_sta(self):
        url = "https://stat-offline.songshuai.com/api/clientdata?content={\"data\":[{\"login_res\":\"登录成功\",\"login_status\":1,\"login_type\":1,\"phone\":15511898673,\"real_name\":\"李泽森\",\"uid\":6860100839851950,\"uname\":\"sn29994lizesen\",\"cellid\":\"\",\"session_id\":\"2020525145606365\",\"ismobiledevice\":\"false\",\"appkey\":\"aac9d32a0eed820769aa1f120e6796db\",\"resolution\":\"1366*768\",\"lac\":\"\",\"network\":\"wire\",\"deviceid\":\"\",\"version\":\"2.1.14\",\"modulename\":\"Administrator\",\"time\":\"2020-05-25 14:56:06\",\"useridentifier\":15511898673,\"lib_version\":\"5.0.0\",\"havegravity\":\"true\",\"platform\":\"win32\",\"havewifi\":\"true\",\"os_version\":\"6.1.7601\",\"phonetype\":\"1\",\"havebt\":\"false\",\"wifimac\":\"\",\"devicename\":\"PC-20190616JUMM\",\"mccmnc\":\"\",\"language\":\"zh\",\"imsi\":\"ia32\",\"salt\":\"8e565b17182b4b57863ee8d7d8847e77\",\"osversion\":\"6.1.7601\",\"account_id\":\"\",\"school_id\":\"\",\"school_name\":\"\"}]}&sign=00CC557E77A24DE32691D7B15BF143B581C2234B"


        # data = {
        #     "content": {"data":[{"login_res":"登录成功","login_status":1,"login_type":1,"phone":15511898673,"real_name":"李泽森","uid":6860100839851950,"uname":"sn29994lizesen","cellid":"","session_id":"2020525145606365","ismobiledevice":"false","appkey":"aac9d32a0eed820769aa1f120e6796db","resolution":"1366*768","lac":"","network":"wire","deviceid":"","version":"2.1.14","modulename":"Administrator","time":"2020-05-25 14:56:06","useridentifier":15511898673,"lib_version":"5.0.0","havegravity":"true","platform":"win32","havewifi":"true","os_version":"6.1.7601","phonetype":"1","havebt":"false","wifimac":"","devicename":"PC-20190616JUMM","mccmnc":"","language":"zh","imsi":"ia32","salt":"8e565b17182b4b57863ee8d7d8847e77","osversion":"6.1.7601","account_id":"","school_id":"","school_name":""}]},
        #     "sign": "704AD94C9EF9D65965AC589528EAADD9F78E9A8"
        #   }


        response = requests.request("POST", url)
        self._printResponse(response)
        return response


amg = AMG()
# sig = amg.get_sign("kehuduanjiaoshi001", "ceshi001")
# sig1=str(sig)
# print(sig1)
# print(type(sig1))
# amg.login_tea("kehuduanjiaoshi001", "ceshi001", sig=sig1)
# sig1 = amg.get_sign_sta()
# sig2 = str(sig1)
# print(sig2)

# list_a = {"data":[{"login_res":"登录成功","login_status":1,"login_type":1,"phone":15511898673,"real_name":"李泽森","uid":6860100839851950,"uname":"sn29994lizesen","cellid":"","session_id":"2020525145606365","ismobiledevice":"false","appkey":"aac9d32a0eed820769aa1f120e6796db","resolution":"1366*768","lac":"","network":"wire","deviceid":"","version":"2.1.14","modulename":"Administrator","time":"2020-05-25 14:56:06","useridentifier":15511898673,"lib_version":"5.0.0","havegravity":"true","platform":"win32","havewifi":"true","os_version":"6.1.7601","phonetype":"1","havebt":"false","wifimac":"","devicename":"PC-20190616JUMM","mccmnc":"","language":"zh","imsi":"ia32","salt":"8e565b17182b4b57863ee8d7d8847e77","osversion":"6.1.7601","account_id":"","school_id":"","school_name":""}]}
sig3 = '704AD94C9EF9D65965AC589528EAADD9F78E9EA'
res = amg.login_sta()
print(res)



