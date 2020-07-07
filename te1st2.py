import json


def get_sign_sta():
    data = {

        "content": [{"login_res":"登录成功","login_status":1,"login_type":1,"phone":15511898673,"real_name":"李泽森","uid":6860100839851950,"uname":"sn29994lizesen","cellid":"","session_id":"2020525145606365","ismobiledevice":"false","appkey":"aac9d32a0eed820769aa1f120e6796db","resolution":"1366*768","lac":"","network":"wire","deviceid":"","version":"2.1.14","modulename":"Administrator","time":"2020-05-25 14:56:06","useridentifier":15511898673,"lib_version":"5.0.0","havegravity":"true","platform":"win32","havewifi":"true","os_version":"6.1.7601","phonetype":"1","havebt":"false","wifimac":"","devicename":"PC-20190616JUMM","mccmnc":"","language":"zh","imsi":"ia32","salt":"8e565b17182b4b57863ee8d7d8847e77","osversion":"6.1.7601","account_id":"","school_id":"","school_name":""}]
          }
    # new_data = sorted(data.items())
    # print(new_data)
    new_Data = json.loads(data)
    print(type(new_Data))

get_sign_sta()