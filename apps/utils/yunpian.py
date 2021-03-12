import requests
import json


class YunPian(object):
    def __init__(self, apikey):
        self.apikey = apikey
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.apikey,
            "mobile": mobile,
            "text": "【前端学习demo】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }
        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict
