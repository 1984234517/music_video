# import tushare as ts
#
# data = ts.get_hist_data('600519', start='2020-07-30')
# print(data)
# data.to_csv('maotai.csv')

from hashlib import md5

ss = "timestamp=1602155252&word=薛之谦0b50b02fd0d73a9c4c8c3a781c30845f"
updata_str = "timestamp=16021552520b50b02fd0d73a9c4c8c3a781c30845f"
temp = md5()
temp1 = md5()
print(temp)
temp.update(ss.encode('utf-8'))
print(temp.hexdigest())