import requests
from lxml import etree

def request(url, method="GET", params=None, encoding="GBK"):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'}
    result = requests.request(method=method, url=url, params=params, headers=headers)
    result.encoding = encoding
    if result.status_code == 200:
        return etree.HTML(result.text)
    return None


class Data:

    @staticmethod
    def chapter(book_id, chapter_id):
        return request(url="https://www.qu-la.com/booktxt/{}/{}.html".format(book_id, chapter_id))

    @staticmethod
    def book(book_id):
        return request(url="https://www.qu-la.com/booktxt/{}".format(book_id))

    @staticmethod
    def search(keyword):
        params = {"ie": "utf-8", "siteid": "qu-la.com", "q": keyword}
        return request(url="https://so.biqusoso.com/s1.php", params=params, encoding='utf-8')

    @staticmethod
    def rank(page: int, rank_type:str):
        print("https://www.qu-la.com/{}/p{}".format(rank_type, page))
        if page > 1:
            return request(url="https://www.qu-la.com/{}/p{}".format(rank_type, page))
        return request(url="https://www.qu-la.com/allvisit/", encoding='gbk')

    @staticmethod
    def book_class(page: int,  type_name:str):
        if page > 1:
            return request(url="https://www.qu-la.com/{}/p{}".format(type_name, page))
        return request(url="https://www.qu-la.com/{}/".format(type_name))
