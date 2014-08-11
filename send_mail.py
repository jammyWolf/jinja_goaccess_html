#encoding: utf-8
import smtplib  
from email.mime.text import MIMEText  
from global_path import mail_host, mail_user, mail_pass, mail_postfix

def send_mail(to_list, sub, service, content):
    me=sub+": "+service+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, _subtype='html', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
