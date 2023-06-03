import zmail
from config import USERNAME, PASSWORD, MAIL_HOST, MAIL_PORT, SMTP_TLS, SMTP_SSL


def send_mail(target, subject, content):
    server = zmail.server(username=USERNAME,
                          password=PASSWORD,
                          smtp_host=MAIL_HOST,
                          smtp_port=MAIL_PORT,
                          smtp_ssl=SMTP_SSL,
                          smtp_tls=SMTP_TLS)
    if server.send_mail(target, {'subject': subject, 'content_text': content}):
        print('邮件发送成功')
    else:
        print('邮件发送失败')
    
