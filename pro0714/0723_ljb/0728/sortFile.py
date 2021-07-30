#author_='xqh';
#date: 2021/7/28 17:04

import pandas as pd


# data_test = pd.read_excel('a.xlsx')
data_test = pd.read_excel('a.xlsx',engine='openpyxl')

df = pd.DataFrame(data_test)

# 处理数据，去除了第一行列 且下标从0，0开始
# iloc函数 只接受整型参数
print(df.iloc[1,1])


# 获取数据集
data=df.values
for row_v in data:
    # print(row)
    for v in row_v:
        print(v,end=' ')
    print()

# 以列''的标签列来进行升序排列
df_1 = df.sort_values(['c1','c2','c3'],ascending=True)

writer =  pd.ExcelWriter('a.xlsx')
df_1.to_excel(writer,sheet_name = 'Sheet1',index=False)
writer.save()