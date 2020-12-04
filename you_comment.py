import requests
import pymongo
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
client = pymongo.MongoClient('localhost', 27017)
bra_info = client['brainfo']
bra_analy = bra_info['braanaly']

def search_keywork(keyword):
    product_id = []
    # urls = ['https://you.163.com/xhr/search/search.json?keywork=文胸&page={}'.format(str(i)) for i in range(1,4)]
    url = 'https://you.163.com/xhr/search/search.json'
    query = {
        "keyword": keyword,
        "page": 1
    }
    try:
        # for url in urls:
        res = requests.get(url, params=query, headers=headers).json()
        results = res['data']['directly']['searcherResult']['result']
        for result in results:
            product_id.append(result['id'])
        return product_id
    except:
        raise

#函数参数为某一个产品id
def get_comments(product_id):
    urls = ['https://you.163.com/xhr/comment/listByItemByTag.json?itemId={}'.format(product_id) + '&page={}'.format(str(i)) for i in range(1, 50)]
    # pro_comments = []
    try:
        for url in urls:
            comments = requests.get(url, headers=headers).json()
            if not comments['data']['commentList']:
                break
            # print("爬取商品 %s 评论信息" % product_id )
            commentList = comments['data']['commentList']
            bra_analy.insert_many(commentList)
            time.sleep(0.1)
            # try:
            #     # braanaly.insert_many(pro_comments)
            # except:
            #     continue
    except:
        raise

if __name__ == '__main__':
    keyword ='文胸'
    product_ids = search_keywork(keyword)
    for product_id in product_ids:
        get_comments(product_id)






