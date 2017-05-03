# coding=utf-8
from lxml import html
from .config import headers, pid_url, manga_url, search_save_dir, search_url
import os
import requests
import time


table = str.maketrans("|\\?*<\":>+[]/　.'",'。'*15)  # 过滤不能创建文件的字符


def GetSearchPic(uid, session, pid, star='', author_save_dir='', search_save_dir=''):
    pid_home = pid_url + pid  # 获得pid所在url
    manga_home = manga_url + pid  # 获得manga的url
    try:
        image_html = session.get(pid_home)
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        image_html = session.get(pid_home)
    pic_tree = html.fromstring(image_html.text)
    img_node = pic_tree.xpath('//div[@class="wrapper"]/img[@class="original-image"]')  # 获得img节点
    if len(img_node):
        pic_name = img_node[0].get('alt')  # 获得图片名
        pic_url = img_node[0].get('data-src')  # 获得图片url
        if star:
            name = search_save_dir + star + '-' + uid + '-' + pid + '-' + pic_name.translate(table) + '.jpg'
        else:
            name = author_save_dir + uid + '-' + pid + '-' + pic_name.translate(table) + '.jpg'
        get_pic = session.get(pic_url, headers=headers)
        with open(name, 'wb') as f:
            f.write(get_pic.content)
            f.close()
        print(name + ' saved')
    else:
        manga_html = session.get(manga_home)
        manga_tree = html.fromstring(manga_html.text)
        manga_pic_node = manga_tree.xpath('//img[@data-filter="manga-image"]') # 获得manga图片节点
        manga_name = pic_tree.xpath('//h1[@class="title"]/text()')[0]
        if star:
            save_dir = search_save_dir + star + '-' + manga_name.translate(table)
        else:
            save_dir = author_save_dir + manga_name.translate(table)
        if os.path.exists(save_dir):
            pass
        else:
            os.mkdir(save_dir)
            for i in range(manga_pic_node.__len__()):
                try:
                    get_manga_pic = session.get(manga_pic_node[i].get('data-src'),headers=headers)
                except requests.exceptions.ConnectionError:
                    time.sleep(5)
                    get_manga_pic = session.get(manga_pic_node[i].get('data-src'), headers=headers)
                save_name = save_dir + '/' + str(i) + '.jpg'
                with open(save_name, 'wb') as f:
                    f.write(get_manga_pic.content)
                    f.close()
                print(save_name + ' saved')


def searchstart(s, collection, search_key):
    os.mkdir(search_save_dir + search_key)
    num = searchpage(s, search_key)
    if num > 1000:
        num = 1000
    else:
        pass
    for i in range(1, num):
        print('现在是%s页' % i)
        try:
            r_search = s.get(search_url % search_key + str(i))
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            r_search = s.get(search_url % search_key + str(i))
        tree_search = html.fromstring(r_search.text)
        el2 = tree_search.xpath('//ul[@class="count-list"]/li/a')  # 获得收藏数的节点
        for k in range(el2.__len__()):
            img = el2[k].xpath('../../../a/div/img')  # 获得图片节点
            pid = img[0].get('data-id')  # 获得pid
            uid = img[0].get('data-user-id')  # 获得作者uid
            star = el2[k].text_content()  # 获得收藏数
            if (int(star) > int(collection)):
                GetSearchPic(pid=pid, uid=uid, session=s, star=star, search_save_dir=search_save_dir + search_key + '/')
    s.close()


def searchpage(session,search_key):
    r_search = session.get(search_url % search_key + str(1))
    tree = html.fromstring(r_search.text)
    num = (int(tree.xpath('//span[@class="count-badge"]')[0].text[0:-1]) + 2) / 20 + 2
    return int(num)

