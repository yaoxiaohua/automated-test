# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os
import time


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
reportpath = PATH("../Report/")

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(**kwargs):
    '''
    :param f: 附件路径
    :param receiver:发给的人 []
    :return:
    '''
    sender = kwargs["mail_sender"]
    password = kwargs["mail_pwd"]
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('来自<%s>接口测试' % sender)
    msg['To'] = _format_addr(' <%s>' % kwargs["receiver"])
    msg['Subject'] = Header(kwargs["header_msg"], 'utf-8').encode()
    msg.attach(MIMEText(kwargs["ContentTXT"], 'plain', 'utf-8'))

    if kwargs.get("report", "0") != "0":
        part = MIMEApplication(open(kwargs["report"], 'rb').read())
        part.add_header(
            'Content-Disposition',
            'attachment',
            filename=(
                'gb2312',
                '',
                kwargs["report_name"]))
        msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, kwargs["port"])
    server.set_debuglevel(1)
    server.login(sender, password)
    server.sendmail(sender, kwargs["receiver"], msg.as_string())
    server.quit()
    print('Email has send out')

# 查找目录下最新生成的测试报告,返回最新报告的详细路径
def find_Report(reportpath):
    lists = os.listdir(reportpath)
    lists.sort(key=lambda fn: os.path.getmtime(reportpath + "\\" + fn))
    newfile = os.path.join(reportpath, lists[-1])
    print(newfile)
    return newfile


if __name__ == '__main__':
    receiver = "3210367040@qq.com"
    mail_host = "smtp.qq.com"
    mail_sender = "3210367040@qq.com"
    mail_pwd = "midpdfyfquprdghh"
    port = "465"
    header_msg = "接口测试"
    ContentTXT = "接口测试结果报告，见附件"
    new_report = find_Report(reportpath)
    currentTime = time.strftime('%Y-%m-%d-%H_%M_%S')
    send_mail(
        receiver=receiver,
        mail_host=mail_host,
        mail_sender=mail_sender,
        port=port,
        mail_pwd=mail_pwd,
        header_msg=header_msg,
        report=new_report,
        attach=ContentTXT,
        report_name= currentTime + "测试报告.xlsx")