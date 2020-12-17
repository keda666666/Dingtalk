import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=********'  #接口地址
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "*********"       #内容
        },
        "at":{
            "atMobiles":[
                "12345678910"       #@的人的手机号
            ],
            "isAtAll": True       #是否@ALL
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()
#
#             ┏┓      ┏┓
#            ┏┛┻━━━━━━┛┻┓
#            ┃          ┃
#            ┃  ┳┛   ┗┳ ┃
#            ┃     ┻    ┃
#            ┗━┓      ┏━┛
#              ┃      ┗━━━━━┓
#              ┃  神兽保佑     ┣┓
#              ┃ 永无BUG！     ┏┛
#              ┗┓┓┏━┳┓┏━━━━━┛
#               ┃┫┫ ┃┫┫
#               ┗┻┛ ┗┻┛
