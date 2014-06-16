# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 18:23:29 2013

@author: xujy
"""

import numpy as np
import pylab as pl
import sys
from pylab import *

from tool_funs import *

reload(sys)
sys.setdefaultencoding("utf-8")

zhfont1=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/TrueType/ukai.ttf')

date = sys.argv[1]
#date='20140104'

beta_filename="./data/fileter_ip_infohash_beta_%s"%(date);
beta_data=np.loadtxt(beta_filename, usecols=(3,), dtype=[('ratio', 'f8')])

master_filename="./data/fileter_ip_infohash_master_%s"%(date);
master_data=np.loadtxt(master_filename, usecols=(3,), dtype=[('ratio', 'f8')])

#figure 1

pl.figure(1);

beta_ratio_cdf_data=calc_suc_CDF_data(beta_data['ratio'])
master_ratio_cdf_data=calc_suc_CDF_data(master_data['ratio'])

pl.plot(beta_ratio_cdf_data['x'], beta_ratio_cdf_data['y'], color="red", linewidth=1.0, label=('beta ratio - %d')%(len(beta_ratio_cdf_data)))
pl.plot(master_ratio_cdf_data['x'], master_ratio_cdf_data['y'], color="blue", linewidth=1.0, label=('master ratio - %d')%(len(master_ratio_cdf_data)))

pl.legend(loc='lower right')

pl.xlim(0, 1)
pl.xticks(np.linspace(0, 1, 11, endpoint=True))

pl.xlabel("ip_infohash connect ratio")

pl.ylim(0, 100)
pl.yticks(np.linspace(0, 100, 11, endpoint=True))
pl.ylabel("percentage(%)")

pl.title("ip_infohash connect ratio with gt 30 post in %s"%(date))
pl.grid()

pl.savefig("./png/cdf_of_ip_infohash_connect_ratio_in_%s.png"%(date))

pl.show()

# next: write file
beta_count = 0
for i in beta_ratio_cdf_data['x']:
    if i < 0.01:
        beta_count = beta_count+1

print beta_count

master_count = 0
for i in master_ratio_cdf_data['x']:
    if i < 0.01:
        master_count = master_count+1

print master_count

output_filename="./data/zero_connect_ratio_ip_infohash"
output = open(output_filename, 'a')
output.write("%s %d %d %d %d\n"%(date, len(beta_ratio_cdf_data), beta_count, len(master_ratio_cdf_data), master_count))
output.close()
