# coding = utf-8
"""
@author: jshuzi
@time:2020-12-02
@File: analyse.py
"""

from pymongo import MongoClient
# import pandas as pd
import matplotlib.pyplot as plt

# 链接 mongodb 获取数据
conn = MongoClient('localhost', 27017)
db = conn.brainfo
mongo_collection = db.braanaly

def flush_data(data):
    if 'A' in data:
        return 'A'
    if 'B' in data:
        return 'B'
    if 'C' in data:
        return 'C'
    if 'D' in data:
        return 'D'
    else:
        return 'Else'
# 将数据转换成 DataFrame
# data = pd.DataFrame(list(mongo_collection.find()))
data = mongo_collection.find({}, {"_id":0, "skuInfo": 1})

colors = []
sizes = []
for row in data:
    size = flush_data(row['skuInfo'][1].split(':')[1])
    sizes.append(size)
#     color = flush_data(row['skuInfo'][0].split(':')[1])
#     colors.append(color)

index=["A","B","C","D","Else"]
x = [1,2,3,4,5]
value = []
for i in index:
    num = sizes.count(i)
    value.append(num)

# plt.set_xticklabels(index)

plt.bar(x, height=value, color="red", width=0.5, tick_label=index)
# 获取颜色和尺寸
# skuinfo = data['skuInfo']

# colors = []
# sizes = []
# for row in skuinfo.values.tolist():
#     size = row[1].split(':')[1]
#     sizes.append(size)
#     color = row[0].split(':')[1]
#     colors.append(color)

# df_color = pd.DataFrame(colors, columns=['color'])
# analyse_color = df_color['color'].value_counts()

# df_size = pd.DataFrame(sizes, columns=['size'])
# analyse_size = df_size['size'].value_counts()

# plt.figure(1)
# plt.bar(range(len(analyse_color.index.values.tolist())), analyse_color.values.tolist(), tick_label=analyse_color.index.values.tolist())

# plt.figure(2)
# plt.bar(range(len(analyse_size.index.values.tolist())), analyse_size.values.tolist(), tick_label=analyse_size.index.values.tolist())
# plt.show()
