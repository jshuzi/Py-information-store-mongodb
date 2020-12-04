# coding = utf-8
"""
@author: jshuzi
@time:2020-12-02
@File: analyse.py
"""

from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# 链接 mongodb 获取数据
conn = MongoClient('localhost', 27017)
db = conn.brainfo
mongo_collection = db.braanaly

# 将数据转换成 DataFrame
data = pd.DataFrame(list(mongo_collection.find()))

# 获取颜色和尺寸
skuinfo = data['skuInfo']

colors = []
sizes = []
for row in skuinfo.values.tolist():
    size = row[1].split(':')[1]
    sizes.append(size)
    color = row[0].split(':')[1]
    colors.append(color)

df_color = pd.DataFrame(colors, columns=['color'])
analyse_color = df_color['color'].value_counts()

df_size = pd.DataFrame(sizes, columns=['size'])
analyse_size = df_size['size'].value_counts()

plt.figure(1)
plt.bar(range(len(analyse_color.index.values.tolist())), analyse_color.values.tolist(), tick_label=analyse_color.index.values.tolist())

plt.figure(2)
plt.bar(range(len(analyse_size.index.values.tolist())), analyse_size.values.tolist(), tick_label=analyse_size.index.values.tolist())
plt.show()








