#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
该文件包含图灵机器人自定应答模块
使用商用的图灵机器人实现自动应答
关于图灵机器人详情查看：
http://www.turingapi.com/
'''

import json
import urllib.request

def trulingResponse(text):
    '''
    使用图灵机器人实现自动应答
    '''
    req_url = 'http://openapi.tuling123.com/openapi/api/v2'
    req = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": "你好"
            },
        },
        "userInfo": {
            "apiKey": "bbe56978fe0140bba232bfe77212b560",
            "userId": "553827"
        }
    }
    req["perception"]["inputText"]["text"] = text

    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(req_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)

    results = response_dic["results"][0]["values"]["text"]
    return results


if __name__ == '__main__':
    while True:
        input_text = input(">>>")
        response_text = trulingResponse(input_text)
        print('Truling Machine Response: '+response_text)
