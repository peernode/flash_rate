#! /usr/bin/env python2.7
#coding=utf-8  
 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
 
# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders
 
import os
import sys

text = ""

def send_mail(text, texts=[], files=[], images=[], date=""): 
    global password
    server={}
    server['name'] = 'mail.funshion.com'
    server['user'] = 'xujy'
    server['passwd'] = 'Zgzbs2018'
    to = ['flashp2p@funshion.com']
    #to = ['xujy@funshion.com']
    fro = "xujy@funshion.com" 
    
    msg3 = MIMEMultipart() 
    msg3['From'] = fro 
    msg3['Subject'] = "flashp2p vod rate analysis %s"%(date)
    msg3['To'] = COMMASPACE.join(to) #COMMASPACE==', ' 
    msg3['Date'] = formatdate(localtime=True) 
    #msg3.attach(MIMEText(text, 'html', 'utf-8'))  

    for a_text in texts:
        text += str(a_text)
			 
    for file in files: 
       part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
       part.set_payload(open(file, 'rb').read()) 
       encoders.encode_base64(part) 
       part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file)) 
       msg3.attach(part)
        
 
    i = 0;
    for image in images:
        text += '<br><img src="cid:image%d">'%i
        
        part = MIMEImage(open(image, 'rb').read())
        part.add_header('Content-ID', '<image%d>'%i)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(image))

        msg3.attach(part)
        i += 1
 
    msg3.attach(MIMEText(text, 'html', 'utf-8'))  
    
    import smtplib 
    smtp = smtplib.SMTP(server['name'])
    smtp.login(server['user'], server['passwd']) 
    msg_content = msg3.as_string()
    smtp.sendmail(fro, to, msg_content) #msg.as_string()
    smtp.close()

def main(date):
    print ("Send mail start")
    #file = open(input_file, "rb")
    #content = file1.read()
	
    img_list=[]
    img_list.append("script/png/post_hour_beta_%s.png"%(date))
    img_list.append("script/png/post_rate_day_beta_%s.png"%(date))
    img_list.append("script/png/post_hour_master_%s.png"%(date))
    img_list.append("script/png/post_rate_day_master_%s.png"%(date))   
    img_list.append("script/png/seed_hour_beta_%s.png"%(date))
    img_list.append("script/png/seed_day_beta_%s.png"%(date))
    img_list.append("script/png/seed_hour_master_%s.png"%(date))
    img_list.append("script/png/seed_day_master_%s.png"%(date))
    #img_list.append("script/png/cdf_of_ip_infohash_connect_ratio_in_%s.png"%(date))
#    img_list.append("script/png/ip_infohash_zero_day_%s.png"%(date))
    send_mail(text, [], [], img_list, date)
    print ("Send Over")

if __name__ == '__main__':
    #main("P2P_cdf.html", "NO-P2P_cdf.html", "flash_dbuffer_stats_by_net_on_20130710.png")
    main(sys.argv[1])
