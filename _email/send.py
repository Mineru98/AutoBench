import platform
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket

def send():
    ip = socket.gethostbyname(socket.getfqdn())
    _os = platform.platform()
    _os_processor = platform.processor()
    msg = MIMEText("IP: "+ip+ "\n운영체제: " + _os + "\n프로세서: " + _os_processor + "\n--------------------------------------\n원본사이트 구조 변경에 따른 에러 예상\n개발자는 확인바랍니다.\n\nhttps://www.cpubenchmark.net/\nhttps://www.videocardbenchmark.net/")
    msg['Subject'] = "Auto Bench Error Email"
    msg['From'] = "email@google.com"
    msg['To'] = "email@google.com"
    
    try:
        with smtplib.SMTP_SSL("smtp.google.com") as smtp:
            smtp.login('id', 'pw')
            smtp.send_message(msg)
            smtp.quit()
    except:
        print("\n")