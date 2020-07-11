from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import time
import json
import requests
from datetime import datetime

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
data.sort(key=lambda x:x['date'])
    
date_list = list()       # 日期
confirm_list = list()    # 确诊
suspect_list = list()    # 疑似
dead_list = list()       # 死亡
heal_list = list()       # 治愈
for item in data:
    month, day = item['date'].split('/')
    date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
    confirm_list.append(int(item['confirm']))
    suspect_list.append(int(item['suspect']))
    dead_list.append(int(item['dead']))
    heal_list.append(int(item['heal']))
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif'] = ['simhei']   # 用来正常显示中文标签

plt.figure(figsize=(12, 8))
plt.title('2019-2020年新冠肺炎疫情曲线图', fontsize=16)

plt.plot(date_list, confirm_list, 'r-', label='确诊')
plt.plot(date_list, confirm_list, 'rs')

plt.plot(date_list, suspect_list, 'b-',label='疑似')
plt.plot(date_list, suspect_list, 'b*')

plt.plot(date_list, dead_list, 'y-', label='死亡')
plt.plot(date_list, dead_list, 'y+')

plt.plot(date_list, heal_list, 'g-', label='治愈')
plt.plot(date_list, heal_list, 'gd')
    
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # 格式化时间轴标注
plt.gcf().autofmt_xdate() # 优化标注（自动倾斜）
plt.grid(axis='x')       # 显示网格
plt.legend() # 显示图例

plt.show()
