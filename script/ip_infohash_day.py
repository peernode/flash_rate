# -*- coding: utf-8 -*-
"""
Created on 2013/10/31

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
zhfont1=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/TrueType/ukai.ttf')

filetime=sys.argv[1]
filename="./data/zero_connect_ratio_ip_infohash"

data = np.loadtxt(filename, dtype=[('time','i8'),('beta_count','f8'),('beta_zero','f8'),('master_count','f8'),('master_zero','f8')])

data_len=len(np.atleast_1d(data))
time_str=[]
if data_len==1:
    time_str.append(str(data["time"])[4:8])
else:
    for i in range(data_len):
        time_str.append(str(data["time"][i])[4:8])

fig=plt.figure(figsize=(10,6),dpi=120)

plt.plot(data["beta_count"],"*-b",label=u"beta ip_infohash数")
plt.plot(data["master_count"],"^-.b",label=u"master ip_infohash数")
#plt.xlabel(u"单位： date ",fontproperties=zhfont1)
plt.ylabel(u"ip_infohash数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)

ax1=plt.gca()
ax1.set_xlim(0, data_len)
ax1.set_xticks(np.linspace(0, data_len, data_len+1, endpoint=True))
ax1.set_xticklabels(time_str, rotation=75)

ax2=ax1.twinx()
plt.plot(data["beta_zero"]/(data["beta_count"]),"*-r",label=u"beta连接成功率为0比例")
plt.plot(data["master_zero"]/(data["master_count"]),"^-.r",label=u"master连接成功率为0比例")
plt.ylabel(u"连接成功率为0比率",fontproperties=zhfont1)
plt.ylim(0,0.8)
plt.legend(loc="upper right",prop=zhfont1)
plt.grid()

plt.title(u"按ip_infohash统计连接成功率为0",fontproperties=zhfont1)

plt.savefig("./png/ip_infohash_zero_day_"+filetime)

print "draw"+filetime+" beta-master date png"
