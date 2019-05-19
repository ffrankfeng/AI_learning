import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 1
unrate = pd.read_csv('../resources/unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE']) # 类型转换
# print(unrate.head(10))
#
# first_twelve = unrate[0:12]
# plt.plot(first_twelve['DATE'],first_twelve['VALUE']) # x轴是date，y轴是value
# plt.show()
#
# plt.plot(first_twelve['DATE'],first_twelve['VALUE']) # x轴是date，y轴是value
# plt.xticks(rotation=45)  # x轴标记旋转45度
# plt.show()
#
# plt.plot(first_twelve['DATE'],first_twelve['VALUE']) # x轴是date，y轴是value
# plt.xticks(rotation=90)
# plt.xlabel("Month")
# plt.ylabel("Unemployment Rate")
# plt.title("Monthly Unemployment Trends,1948")
# plt.show()

# 2
# fig = plt.figure()
# ax1 = fig.add_subplot(4,3,1)
# ax2 = fig.add_subplot(4,3,2)
# ax3 = fig.add_subplot(4,3,6)
# plt.show()

# 3
# fig = plt.figure(figsize=(3,6))
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
#
# ax1.plot(np.random.randint(1,5,5),np.arange(5))
# ax2.plot(np.arange(5)*3,np.arange(5))
# plt.show()

# 4 画多条线
unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))

plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c='red')
plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c='black')
plt.show()