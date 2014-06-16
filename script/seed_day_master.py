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
filename="./data/seed_day_master"

data = np.loadtxt(filename, dtype=[('time','i8'),('mv_t','f8'),('mv_s','f8'),('tv_t','f8'),('tv_s','f8'),('cartoon_t','f8'),('cartoon_s','f8')])

data_len=len(np.atleast_1d(data))
time_str=[]
if data_len==1:
    time_str.append(str(data["time"])[4:8])
else:
    for i in range(data_len):
        time_str.append(str(data["time"][i])[4:8])

fig=plt.figure(figsize=(10,6),dpi=120)

plt.plot(data["mv_t"],"*-b",label=u"电影种子数")
plt.plot(data["tv_t"],"^-.b",label=u"电视剧种子数")
plt.plot(data["cartoon_t"],"o-.b",label=u"卡通种子数")
plt.ylabel(u"种子数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)

ax1=plt.gca()
ax1.set_xlim(0, data_len)
ax1.set_xticks(np.linspace(0, data_len, data_len+1, endpoint=True))
ax1.set_xticklabels(time_str, rotation=75)

ax2=ax1.twinx()
plt.plot(data["mv_s"]/(data["mv_t"]),"*-r",label=u"电影可做种率")
plt.plot(data["tv_s"]/(data["tv_t"]),"^-.r",label=u"电视剧可做种率")
plt.plot(data["cartoon_s"]/(data["cartoon_t"]),"o-r",label=u"卡通可做种率")
plt.ylabel(u"可做种率",fontproperties=zhfont1)
plt.ylim(0, 1.0)
ax2.set_yticks(np.linspace(0, 1, 11))
plt.legend(loc="lower left",prop=zhfont1)
plt.grid()

plt.title(u"【Master版本】可做种率",fontproperties=zhfont1)

plt.savefig("./png/seed_day_master_"+filetime)

print "draw"+filetime+" master date png"
