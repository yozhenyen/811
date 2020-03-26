import pandas as pd
#
# data_list = []
#
# df_new = pd.DataFrame()
#
# for i in range (1, 13):
#     df = pd.read_csv(f'123ＣＤツリ｜ハウス-2012-{i}.csv')
#     data_list.append(df)
#
# con = pd.concat(data_list, axis=1, ignore_index=True)
#
# df_new = pd.DataFrame(con)
#
# df_new.to_csv('concattime.csv', index=False)
#
#
#
# print(df_new)
df = pd.read_csv('concattime.csv')
df1 = df.iloc[:1,:].values[0]
col = pd.unique(df1)
# df = list(set(df1))
print(len(col))


