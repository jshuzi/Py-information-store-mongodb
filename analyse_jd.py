import pymongo
import matplotlib.pyplot as plt


client = pymongo.MongoClient('localhost', 27017)
# jd数据库
db = client.jd
# product表,没有自动创建
product_db = db.product
# 统计以下几个颜色
color_arr = ['肤色', '黑色', '紫色', '粉色', '蓝色', '白色', '灰色', '香槟色', '红色']

color_num_arr = []
for i in color_arr:
    num = product_db.count({'product_color': i})
    color_num_arr.append(num)

# 显示的颜色
# color_arr = ['bisque', 'black', 'purple', 'pink', 'blue', 'white', 'gray', 'peru', 'red']
# patches,l_text,p_text = plt.pie(color_num_arr, labels=color_arr,
#                                 labeldistance=1.1, autopct='%3.1f%%', shadow=False,
#                                 startangle=90, pctdistance=0.6)
# #改变文本的大小
# #方法是把每一个text遍历。调用set_size方法设置它的属性
# for t in l_text:
#     t.set_size=(30)
# for t in p_text:
#     t.set_size=(20)
# # 设置x，y轴刻度一致，这样饼图才能是圆的
# plt.axis('equal')
# plt.title("内衣颜色比例图", fontproperties="SimHei") #
# plt.legend()
# plt.figure(1)
# plt.show()

index=["A","B","C","D","Else"]
x = [1,2,3,4,5]

value = []
for i in index:
    num = product_db.count({'product_size': i})
    value.append(num)
plt.bar(x, height=value, color="red", width=0.5, tick_label=index)
total = sum(value)
for a, b in zip(x, value):
    partial = float(b/total)
    plt.text(a, b + 0.05, '%.4f' % partial, ha='center', va='bottom', fontsize=10)
# plt.figure(2)
plt.show()

