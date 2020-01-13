#!/usr/bin/env python

#-*-coding:utf-8-*-

'''使用有道翻译网站完成翻译功能模块
    该模块包含两个函数

    一下为语言的简写，fromlanguage和tolanguage可以使用该简写
'''

from urllib import request, parse
import json

def youDaoTranslate(text, fromlanguage = 'AUTO', tolanguage = 'AUTO'):
    '''把fromlanguage语言的text翻译成tolanguage对应的译文，
        若未指定语言则自动检测语言类型并翻译成中文
        fromelanguage：待翻译的text所属语言
        text：待翻译文本
        tolanguage：翻译结果所属语言'''
    req_url = 'http://fanyi.youdao.com/translate'
    Form_Date = {
        'action':'FY_BY_REALTIME',
        'client':'fanyideskweb',
        'doctype':'json',
        'from':fromlanguage,
        'i':text,
        'keyfrom':'fanyi.web',
        'smartresult':'dict',
        'to':tolanguage,
        'version':'2.1'
    } #创建网站输入信息

    data = parse.urlencode(Form_Date).encode('utf-8')
    response = request.urlopen(req_url, data)
    html = response.read().decode('utf-8')
    #得到有道翻译返回的信息，json编码

    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    return translate_results


if __name__ == '__main__':
    while True:
        from_ = input("From Language> ")
        text = input("The text to translate> ")
        to_ = input("To Language> ")
        print(youDaoTranslate(text, from_, to_))
