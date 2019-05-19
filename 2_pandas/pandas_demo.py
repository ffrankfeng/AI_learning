import pandas
food_info = pandas.read_csv("../resources/food_info.csv")
# print(food_info)
print(food_info.dtypes)#有哪些数据类型
#显示头、尾10条数据
print(food_info.head(10))
print(food_info.tail(10))
print(food_info.columns)#列名（第一行作为列名）
print(food_info.shape)#维度

print(food_info.loc[0])#取第一条数据
print(food_info.loc[3:6])#取第3-6条数据
#按列名取值
col_list=["NDB_No","Shrt_Desc"]
print(food_info[col_list])

col_names = food_info.columns.tolist()
print(col_names)
gram_columns = []
for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
print(gram_columns)

# water_energry = food_info["Water_(g)"] * food_info["Enterg_Kcal"]
iron_gtams = food_info["Iron_(mg)"]
#向food_info中加入新数据
food_info["my_Iron_(g)"] =iron_gtams/1000