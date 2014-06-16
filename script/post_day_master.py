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
filename="./data/post_rate_day_master"

data = np.loadtxt(filename, dtype=[('time','i8'),('post','f8'),('succ','f8'),('fail','f8'),('post_1st','f8'),('succ_1st','f8'),('fail_1st','f8')])

data_len=len(np.atleast_1d(data))
time_str=[]
if data_len==1:
    time_str.append(str(data["time"])[4:8])
else:
    for i in range(data_len):
        time_str.append(str(data["time"][i])[4:8])

fig=plt.figure(figsize=(10,6),dpi=120)

plt.plot(data["post"],"*-b",label=u"主动投递数")
plt.plot(data["post_1st"],"^-.b",label=u"首次主动投递数")
#plt.xlabel(u"单位： date ",fontproperties=zhfont1)
plt.ylabel(u"主动投递数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)

ax1=plt.gca()
ax1.set_xlim(0, data_len)
ax1.set_xticks(np.linspace(0, data_len, data_len+1, endpoint=True))
ax1.set_xticklabels(time_str, rotation=75)

ax2=ax1.twinx()
plt.plot(data["succ"]/(data["post"]),"*-r",label=u"连接成功率")
plt.plot(data["succ_1st"]/(data["post_1st"]),"^-.r",label=u"首次投递连接成功率")
plt.plot(data["fail"]/(data["post"]),"o-r",label=u"服务器通知不存在比率")
plt.ylabel(u"连接成功率/服务器通知不存在比率",fontproperties=zhfont1)
plt.ylim(0,0.8)
plt.legend(loc="upper right",prop=zhfont1)
plt.grid()

plt.title(u"【主版本】peer连接成功率",fontproperties=zhfont1)

plt.savefig("./png/post_rate_day_master_"+filetime)

print "draw"+filetime+" master date png"
