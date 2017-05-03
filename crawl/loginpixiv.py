# coding=utf-8
import requests
from lxml import html
from .config import LOGIN_URL,data,headers


def login():
    s = requests.session()
    r = s.get(LOGIN_URL)
    tree = html.fromstring(r.text)
    el1 = tree.xpath('//input[@name="post_key"]')[0]
    post_key = el1.value
    id = input('Please input your pivix id:')
    passwd = input('Please input your password:')
    data['pixiv_id'] = id
    data['password'] = passwd
    data['post_key'] = post_key
    r = s.post(LOGIN_URL, headers=headers, data=data)
    if r.url == 'https://www.pixiv.net/':
        print('Login success!')
    else:
        print('Login failed.')
        exit(0)
    return s

