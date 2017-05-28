# Pixivcrawl
Your can use this tool to get pixiv picture!

两个库：

pip instasll requests

pip install lxml


版本python3.6

-h, --help            show this help message and exit

-u UID, --uid UID     输入p站作者id就能把他们所有的图都拿下来啦

-s SEARCH, --search SEARCH 输入你要搜索的东西并且使用-c可以筛选出你要的收藏数的图。最好使用日文哦。

-c COLLECTION, --collection COLLECTION 一定要配合-s使用哦

-i, --init           最先要使用-i在你的D盘创建初始文件


爬取的过程中报错了，那么肯定是网络问题，如果获取的还不多的话，那么就删掉文件夹重新爬，如果爬的多的话，看一下爬到哪一页了，在代码里改一下

例：
python setup -i

python setup -u xxxxxxx

python setup -s xxx -c 100
