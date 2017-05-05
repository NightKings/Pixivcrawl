# coding=utf-8

LOGIN_URL = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
pid_url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id='
manga_url = 'https://www.pixiv.net/member_illust.php?mode=manga&illust_id='
search_save_dir = 'D:/Picture/pixiv/'
author_save_dir = 'D:/Picture/pixiv/'
search_url = 'https://www.pixiv.net/search.php?word=%s&order=date_d&p='


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://accounts.pixiv.net',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/57.0.2987.133 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
    'Accept-Encoding': 'gzip, deflate, br'
}
data = {
    'captcha':'',
    'g_recaptcha_response':'',
    'password': '',
    'pixiv_id': '',
    'post_key': '',
    'ref': 'wwwtop_accounts_index',
    'return_to': 'https://www.pixiv.net/',
    'source': 'pc'
}
