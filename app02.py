import streamlit as st
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def app():

    #Gmailを送付
    st.subheader("app / Send Gmail")

    st.subheader("Delivery address")
    #left_column,right_column = st.columns(2)
    left_column,right_column = st.columns([1,5])
    select = left_column.selectbox("Reji or New",(" ","Reji","New"))
    if select == "Reji":
        to_address = right_column.selectbox('Pls select mail-address',(" ",'tomotaka.a@gmail.com','slimefarm0304@gmail.com','style.azuma@gmail.com'))
    elif select == "New":
        to_address = right_column.text_input('Pls input mail-address')


    res = st.button("send")
    if res ==True:
        #gmailserverの設定
        #【重要】passwordはgitしない
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = "slimefarmsamplesite@gmail.com"
        smtp_password = st.secrets["PASSWORD"]

        #メール文書の設定
        #to_address = "送付先アドレス"
        from_address = smtp_user
        subject = "タイトル"
        body = "本文"
        filepath = "C:/Users/slime/Desktop/sample.txt"
        filename = os.path.basename(filepath)

        #メール文書を送付用データ（添付ファイル付）を生成
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_address
        msg["To"] = to_address
        msg.attach(MIMEText(body))
        with open(filepath, "rb") as f:
            mb = MIMEApplication(f.read())
        mb.add_header("Content-Disposition", "attachment", filename=filename)
        msg.attach(mb)

        #メールを送付
        s = smtplib.SMTP(smtp_server, smtp_port)
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(from_address, to_address, msg.as_string())
        s.quit()