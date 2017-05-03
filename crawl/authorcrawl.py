# coding=utf-8
from .searchcrawl import GetSearchPic, table
from lxml import html
from .config import author_save_dir
import os

author_url = r'https://www.pixiv.net/member_illust.php?id=%s&type=all&p='


def AuthorStart(session, uid):
    author_home = author_url % uid
    r = session.get(author_home + str(1))
    author_home_tree = html.fromstring(r.text)
    name = author_home_tree.xpath('//h1[@class="user"]/text()')[0]
    os.mkdir(author_save_dir + name.translate(table))
    num = authorpage(session,uid)
    if num > 1000:
        num = 1000
    else:
        pass
    for i in range(1, num):
        r = session.get(author_home+str(i))
        author_home_tree = html.fromstring(r.text)
        img_node = author_home_tree.xpath('//li[@class="image-item"]/a/div/img')
        for img in img_node:
            pid = img.get('data-id')
            GetSearchPic(pid=pid, uid=uid, session=session, author_save_dir=author_save_dir + name.translate(table)+ '/')



def authorpage(session,uid):
    r_uid = session.get(author_url % uid + '1')
    tree = html.fromstring(r_uid.text)
    num = (int(tree.xpath('//span[@class="count-badge"]')[0].text[0:-1]) + 2) / 20 + 2
    return int(num)