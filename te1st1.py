import hashlib
import requests
import json
class aaa:

  def get_sign_sta(self):
            data = {
                "content": {"data": [{"login_res":"登录成功","login_status":1,"login_type":1,"phone":15511898673,"real_name":"李泽森","uid":6860100839851950,"uname":"sn29994lizesen","cellid":"","session_id":"2020525145606365","ismobiledevice":"false","appkey":"aac9d32a0eed820769aa1f120e6796db","resolution":"1366*768","lac":"","network":"wire","deviceid":"","version":"2.1.14","modulename":"Administrator","time":"2020-05-25 14:56:06","useridentifier":15511898673,"lib_version":"5.0.0","havegravity":"true","platform":"win32","havewifi":"true","os_version":"6.1.7601","phonetype":"1","havebt":"false","wifimac":"","devicename":"PC-20190616JUMM","mccmnc":"","language":"zh","imsi":"ia32","salt":"8e565b17182b4b57863ee8d7d8847e77","osversion":"6.1.7601","account_id":"","school_id":"","school_name":""}]}
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
            list3 = list2.replace('\'', '\"\" ')
            print(list1)
            print(list2)
            print(type(list2))
            print(list3)
            #
            sha = hashlib.sha1(list3.encode('utf-8'))
            sha1 = sha.hexdigest()
            sha2 = sha1.upper()
            #
            print(sha)
            print(sha1)
            print(sha2)
            # return sha2
            # return list2

    # 统计接口登录

  def login_sta(self, content, sig):
        self.s = requests.session()
        data = {
            "content": content,
            "sign": sig
        }
        response = self.s.post("https://stat-offline.songshuai.com/api/clientdata", data=data)
        self._printResponse(response)
        return response

bbb = aaa
bbb.get_sign_sta()
print(bbb)