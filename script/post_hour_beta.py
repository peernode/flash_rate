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
filename="./data/post_rate_hour_beta_"+filetime

data = np.loadtxt(filename, dtype=[('time','i8'),('post','f8'),('succ','f8'),('fail','f8'),('post_1st','f8'),('succ_1st','f8'),('fail_1st','f8')])


fig=plt.figure(figsize=(10,6),dpi=120)
ax1=fig.add_subplot(111)

plt.plot(data["time"],data["post"],"*-b",label=u"主动投递数")
plt.plot(data["time"],data["post_1st"],"^-.b",label=u"首次主动投递数")
plt.xlabel(u"单位： Hour ",fontproperties=zhfont1)
plt.ylabel(u"主动投递数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)
plt.grid()

ax2=ax1.twinx()
plt.plot(data["time"],data["succ"]/(data["post"]),"*-r",label=u"连接成功率")
plt.plot(data["time"],data["succ_1st"]/(data["post_1st"]),"^-.r",label=u"首次投递连接成功率")
plt.plot(data["time"],data["fail"]/(data["post"]),"o-r",label=u"服务器通知不存在比率")
plt.ylabel(u"连接成功率/服务器通知不存在比率",fontproperties=zhfont1)
plt.ylim(0,0.8)
plt.legend(loc="upper right",prop=zhfont1)
plt.grid()

plt.xlim(0,24)
plt.xticks(range(24))
plt.title(u"【Beta版本】peer连接成功率"+filetime,fontproperties=zhfont1)

plt.savefig("./png/post_hour_beta_"+filetime)

print "draw"+filetime+" beta hour png"
