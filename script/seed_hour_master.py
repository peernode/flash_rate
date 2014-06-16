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
filename="./data/seed_hour_master_"+filetime

data = np.loadtxt(filename, dtype=[('time','i8'),('mv_t','f8'),('mv_s','f8'),('tv_t','f8'),('tv_s','f8'),('cartoon_t','f8'),('cartoon_s','f8')])

fig=plt.figure(figsize=(10,6),dpi=120)
ax1=fig.add_subplot(111)

plt.plot(data["time"],data["mv_t"],"*-b",label=u"mv种子数")
plt.plot(data["time"],data["tv_t"],"^-.b",label=u"tv种子数")
plt.plot(data["time"],data["cartoon_t"],"o-.b",label=u"cartoon种子数")
plt.xlabel(u"单位： Hour ",fontproperties=zhfont1)
plt.ylabel(u"连接成功种子数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)
plt.grid()

ax2=ax1.twinx()
plt.plot(data["time"],data["mv_s"]/(data["mv_t"]),"*-r",label=u"mv可做种率")
plt.plot(data["time"],data["tv_s"]/(data["tv_t"]),"^-.r",label=u"tv可做种率")
plt.plot(data["time"],data["cartoon_s"]/(data["cartoon_t"]),"o-r",label=u"cartoon可做种率")
plt.ylabel(u"可做种率",fontproperties=zhfont1)
plt.ylim(0,1)
ax2.set_yticks(np.linspace(0, 1, 11))
plt.legend(loc="lower left",prop=zhfont1)
plt.grid()

plt.xlim(0,24)
plt.xticks(range(24))
plt.title(u"【Master版本】种子可做种率"+filetime,fontproperties=zhfont1)

plt.savefig("./png/seed_hour_master_"+filetime)

print "draw"+filetime+" seed hour master png"
