from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from flask_cors import CORS  # 引入 CORS 库
import os

app = Flask(__name__)
CORS(app)  # 允许所有来源访问

# 加载环境变量
load_dotenv()

# 邮件配置信息
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "projectuse213@gmail.com"
SMTP_PASSWORD = "xxxxxxxxx"
EMAIL_FROM = SMTP_USERNAME
EMAIL_TO = "qifanc666@gmail.com"  # 将此替换为你希望接收邮件的邮箱


@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    message_content = data.get('message')

    # 创建邮件内容
    subject = f"New Contact from {first_name} {last_name}"
    body = f"""
    You have a new contact submission.

    First Name: {first_name}
    Last Name: {last_name}
    Email: {email}
    Phone: {phone}
    Message: {message_content}
    """

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接到邮件服务器并发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_FROM, EMAIL_TO, text)
        server.quit()

        return jsonify({"code": 200, "message": "Message sent successfully"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"code": 500, "message": "Something went wrong, please try again later."}), 500


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    email = data.get('EMAIL')

    if not email:
        return jsonify({"code": 400, "message": "Email is required"}), 400

    # 创建邮件内容
    subject = "New Newsletter Subscription"
    body = f"New subscriber: {email}"

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接到邮件服务器并发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_FROM, EMAIL_TO, text)
        server.quit()

        return jsonify({"code": 200, "message": "Subscription successful"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"code": 500, "message": "Something went wrong, please try again later."}), 500


if __name__ == '__main__':
    app.run(debug=True)
