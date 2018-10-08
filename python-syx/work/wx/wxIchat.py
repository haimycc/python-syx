# coding=utf8
import requests
import itchat
import json

KEY = 'eeaa98347259474a865d3aad734d859c'


# headers = {'content-type': 'application/json;charset=UTF-8'}


def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg['Text']
            },
            "selfInfo": {
                "location": {
                    "city": "广东",
                    "province": "深圳",
                    "street": "南山"
                }

            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": 20180931
        }
    }
    try:
        r = requests.post(apiUrl, data=json.dumps(data)).json()
        print(r)
        return r['results'][0]['values']['text']
    except:
        return


@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=True)
def tuling_reply(msg):
    defaultReply = '呵呵'
    print(msg['Text'])
    reply = get_response(msg)
    # 可以自己更改回复前缀
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()
