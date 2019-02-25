import imaplib, email, os
from datetime import datetime
from email.header import decode_header
from email import utils
from configparser import ConfigParser
from initCfg import InitConfig
import os
import re
import sys
from loggingModule import logger

def login(cfg):
    try:
        conn = imaplib.IMAP4_SSL(cfg.emailIP, cfg.emailPort)
        conn.login(cfg.emailUser, cfg.emailPass)
        logger.info ("successful login")
        return conn
    except Exception:
        logger.error("Login Error")
        return None

def emailFetch():
    if getattr(sys, 'frozen', False):
        module_path = os.path.dirname(sys.executable)
    elif __file__:
        module_path = os.path.dirname(__file__)           
    # cfgPath = os.path.join(os.path.dirname(__file__), 'config.ini')
    cfgPath = os.path.join(module_path, 'config.ini')
    cfg = InitConfig(cfgPath)
    conn = login(cfg)

    if conn:
        conn.select("INBOX")
        #提取了文件夹中所有邮件的编号，search功能在本邮箱中没有实现……
        resp, mails = conn.uid('search', None, 'ALL')
        # print(mails[0].split(b' '))
        email_num = len(mails[0].split(b' '))-1
        count = 0
        for message in range(email_num, int(cfg.cutOff), -1):
            resp, data = conn.uid('fetch', mails[0].split(b' ')[message], '(RFC822)')
            mail = email.message_from_bytes(data[0][1])
            flag = False
            sender = utils.parseaddr(mail['FROM'])[1]
            if sender.strip() == "Rainy.Sun@availink.com":
                fileName = 'No Attachment' 
                #获取邮件附件名称
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    fileName = part.get_filename()  

                #如果文件名为纯数字、字母时不需要解码，否则需要解码
                    try:
                        fileName = decode_header(fileName)[0][0].decode(decode_header(fileName)[0][1])
                        if not re.match('PLANNING SUMMARY-\d{8}\.xlsx', fileName):
                            continue
                    except:
                        pass
                #如果获取到了文件，则将文件保存在制定的目录下
                    if fileName != 'No Attachment':
                        filePath = os.path.join(cfg.emailSavePath, fileName)
                        # print (filePath)
                        if not os.path.isfile(filePath):
                            fp = open(filePath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()
                            logger.info ("附件已经下载，文件名为：" + fileName)
                            flag = True
                            count += 1
                            cfg.setCutOff(message)
                            break
                        else:
                            logger.info ("附件已经存在，文件名为：" + fileName)
                            flag = True
                            cfg.setCutOff(message)
                            break
            if flag:
                break
        if count==0:
            logger.info("附件已经存在或本次查询没有找到需下载邮件附件")
        conn.close()
        conn.logout()
        logger.info("successful exit")
    else:
        logger.info ("conn is None")

def emailFetchMain():
    emailFetch()

if __name__ == "__main__":
    emailFetchMain()