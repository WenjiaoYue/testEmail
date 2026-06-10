import os
import ssl
import smtplib
from email.message import EmailMessage


SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.qq.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))

MAIL_SENDER = os.getenv("MAIL_SENDER")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_TO = os.getenv("MAIL_TO")

EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "GitHub Action 测试邮件")
EMAIL_CONTENT = os.getenv("EMAIL_CONTENT", "这是一封由 GitHub Actions 发送的测试邮件。")


def send_email():
    if not MAIL_SENDER:
        raise ValueError("缺少 MAIL_SENDER")
    if not MAIL_PASSWORD:
        raise ValueError("缺少 MAIL_PASSWORD")
    if not MAIL_TO:
        raise ValueError("缺少 MAIL_TO")

    msg = EmailMessage()
    msg["From"] = MAIL_SENDER
    msg["To"] = MAIL_TO
    msg["Subject"] = EMAIL_SUBJECT
    msg.set_content(EMAIL_CONTENT)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(MAIL_SENDER, MAIL_PASSWORD)
        server.send_message(msg)

    print("邮件发送成功")


if __name__ == "__main__":
    send_email()
