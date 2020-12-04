import requests
import pymongo
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Referer': 'https://item.jd.com'
}
client = pymongo.MongoClient('localhost', 27017)
db =client['jd']
collection = db['product']

def find_product_id(key_word):
    jd_url = 'https://search.jd.com/Search'
    product_ids = []
    for i in range(1,6):
        param =
            {
            'keyword': key_word,
             'enc':'utf-8',
             'page':i
             }
        response = requests.get(jd_url, params = param, headers=headers)
        #find all the product ids
        ids = re.findall('data-sku="(.*?)"', response.text, re.S)
        product_ids.append(ids)
    return product_ids

def get_comment_message(product_id):
    urls=['https://club.jd.com/comment/productPageComments.action?'\
          'callback=fetchJSON_comment98&'\
          'productId={}&'\
          'score=0&sortType=5&'\
          'page={}&'\
          'pageSize=10&isShadowSku=0&fold=1'.format(product_id, i) for i in range(1, 11)]
    for url in urls:
        response = requests.get(url, headers=headers)
        html = response.text
        html = html = html.replace('fetchJSON_comment98(', '').replace(');', '')
        data = json.loads(html)
        comments = data['comments']
        for comment in comments:
            product_data = {}
            product_data['product_color'] = flush_data(comment['productColor'])
            product_data['product_size'] = flush_data(comment['productSize'])
            product_data['comment_content'] = comment['content']
            product_data['create_time'] = comment['creationTime']
            collection.insert_one(product_data)

def flush_data(data):
    if '肤' in data:
        return '肤色'
    if '黑' in data:
        return '黑色'
    if '紫' in data:
        return '紫色'
    if '粉' in data:
        return '粉色'
    if '蓝' in data:
        return '蓝色'
    if '白' in data:
        return '白色'
    if '灰' in data:
        return '灰色'
    if '槟' in data:
        return '香槟色'
    if '琥' in data:
        return '琥珀色'
    if '红' in data:
        return '红色'
    if '紫' in data:
        return '紫色'
    if 'A' in data:
        return 'A'
    if 'B' in data:
        return 'B'
    if 'C' in data:
        return 'C'
    if 'D' in data:
        return 'D'

if __name__ == '__main__':
    key_word ='胸罩'
    product_ids = find_product_id(key_word)
    for product_id in product_ids:
        get_comment_message(product_id)
