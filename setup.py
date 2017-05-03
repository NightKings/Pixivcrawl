#  coding = utf-8
import argparse
from crawl.searchcrawl import searchstart
from crawl.loginpixiv import login
from crawl.authorcrawl import AuthorStart
import os


def initdir():
    os.mkdir('D:/Picture/')
    os.mkdir('D:/Picture/search')
    os.mkdir('D:/Picture/author')



def main():
    parser = argparse.ArgumentParser(description='Get pixiv\'s pictures')
    parser.add_argument('-u', '--uid', help='Enter the pixiv\'s author uid,'
                                            'your can get this all the author\'s picture.')
    parser.add_argument('-s', '--search', help='Enter what your want to search the picture(if your want to get anime pictures you should enter Japanese),'
                                               ' it must use with -c', default=None)
    parser.add_argument('-c', '--collection', help='If you search, you need order the collection number to '
                                                   'collect pictures, it must use with -s.', default=None)
    parser.add_argument('-i', '--init', action="store_true", help='Create the directories in D:/.')
    args = parser.parse_args()

    if args.uid:
        AuthorStart(login(), uid=args.uid)
    elif args.collection is None and args.search is not None:
        print('Collection is none please use -c to enter the collection number.')
    elif args.collection is not None and args.search is None:
        print('Search is none please use -s to enter the search key')
    elif args.collection is not None and args.search is not None:
        searchstart(s=login(), collection=args.collection, search_key=args.search)
    elif args.init:
        initdir()
    else:
        print('If your first use this tool, your should ues -i to create directories')



main()
