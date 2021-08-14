from email.mime import text
import streamlit as st
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def app():

    #Gmailを送付
    st.subheader("app / Send Gmail")
 
    #送付先を指定する
    st.subheader("Delivery address")
    #left_column,right_column = st.columns(2)
    left_column,right_column = st.columns([1,4])
    select = left_column.radio("Rejister or New",("Rejister","New"))
    if select == "Rejister":
        to_address = right_column.selectbox('Pls select mail-address',(" ",'tomotaka.a@gmail.com','slimefarm0304@gmail.com','style.azuma@gmail.com'))
    elif select == "New":
        to_address = right_column.text_input('Pls input mail-address')

    #タイトル、本文を確認する
    st.subheader("Message")
    with st.expander("Check the message"):
        option = st.text_input('Recipient name    ex ) 東 , 東京銀行　東')
        subject = "資料送付"
        if bool(option) == True:
            body = option + " 様\n\n資料を送付いたします。\n\nご確認いただきまして、不明な点や不足する点がございましたらご連絡いただけますようお願い申し上げます。\n\nSlimeFarm 東 智隆"
        else:
            body = ("資料を送付いたします。\n\nご確認いただきまして、不明点や不足点がございましたら、ご連絡くださいますようお願い申し上げます。\n\nSlimeFarm 東 智隆")
        
        st.write("件名 / " + subject)
        st.write(body)
        #body = st.write('{0}様\n\nお世話になっております。\n\n{1}をお送りいたします。\n\nご確認ください。\n\nfrom tomotaka'.format(send_name,file_name))

    #添付ファイルを指定する
    st.subheader("Attachment file")
    with st.expander("Select file"):
        left_column, center_column, right_column = st.columns(3)
        file_01 = left_column.checkbox('samplefile_01')
        file_02 = left_column.checkbox('samplefile_02')
        file_03 = left_column.checkbox('samplefile_03')
        file_04 = left_column.checkbox('samplefile_04')

        file_05 = center_column.checkbox('samplefile_05')
        file_06 = center_column.checkbox('samplefile_06')
        file_07 = center_column.checkbox('samplefile_07')
        file_08 = center_column.checkbox('samplefile_08')

        file_09 = right_column.checkbox('samplefile_09')
        file_10 = right_column.checkbox('samplefile_10')
        file_11 = right_column.checkbox('samplefile_11')
        file_12 = right_column.checkbox('samplefile_12')

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
        #subject = "タイトル"
        #body = "本文"
        #st.write('{0}様\n\nお世話になっております。\n\n{1}をお送りいたします。\n\nご確認ください。\n\nfrom tomotaka'.format(send_name,file_name))
        #filepath = "./sample.txt"
        #filename = os.path.basename(filepath)
        filepath01 ="./sample_01.txt"
        filename01 = os.path.basename(filepath01)
        filepath02 ="./sample_02.txt"
        filename02 = os.path.basename(filepath02)
        filepath03 ="./sample_03.txt"
        filename03 = os.path.basename(filepath03)
        filepath04 ="./sample_04.txt"
        filename04 = os.path.basename(filepath04)
        filepath05 ="./sample_05.txt"
        filename05 = os.path.basename(filepath05)
        filepath06 ="./sample_06.txt"
        filename06 = os.path.basename(filepath06)
        filepath07 ="./sample_07.txt"
        filename07 = os.path.basename(filepath07)
        filepath08 ="./sample_08.txt"
        filename08 = os.path.basename(filepath08)
        filepath09 ="./sample_09.txt"
        filename09 = os.path.basename(filepath09)
        filepath10 ="./sample_10.txt"
        filename10 = os.path.basename(filepath10)
        filepath11 ="./sample_11.txt"
        filename11 = os.path.basename(filepath11)
        filepath12 ="./sample_12.txt"
        filename12 = os.path.basename(filepath12)

        #メール文書を送付用データ（添付ファイル付）を生成
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_address
        msg["To"] = to_address
        msg.attach(MIMEText(body))
        #with open(filepath, "rb") as f:
            #mb = MIMEApplication(f.read())
        #mb.add_header("Content-Disposition", "attachment", filename=filename)
        #msg.attach(mb)
        if file_01 == True:
            with open(filepath01, "rb") as f:
                mb01 = MIMEApplication(f.read())
            mb01.add_header("Content-Disposition", "attachment", filename=filename01)
            msg.attach(mb01)
        if file_02 == True:
            with open(filepath02, "rb") as f:
                mb02 = MIMEApplication(f.read())
            mb02.add_header("Content-Disposition", "attachment", filename=filename02)
            msg.attach(mb02)
        if file_03 == True:
            with open(filepath03, "rb") as f:
                mb03 = MIMEApplication(f.read())
            mb03.add_header("Content-Disposition", "attachment", filename=filename03)
            msg.attach(mb03)
        if file_04 == True:
            with open(filepath04, "rb") as f:
                mb04 = MIMEApplication(f.read())
            mb04.add_header("Content-Disposition", "attachment", filename=filename04)
            msg.attach(mb04)
        if file_05 == True:
            with open(filepath05, "rb") as f:
                mb05 = MIMEApplication(f.read())
            mb05.add_header("Content-Disposition", "attachment", filename=filename05)
            msg.attach(mb05)
        if file_06 == True:
            with open(filepath06, "rb") as f:
                mb06 = MIMEApplication(f.read())
            mb06.add_header("Content-Disposition", "attachment", filename=filename06)
            msg.attach(mb06)
        if file_07 == True:
            with open(filepath07, "rb") as f:
                mb07 = MIMEApplication(f.read())
            mb07.add_header("Content-Disposition", "attachment", filename=filename07)
            msg.attach(mb07)
        if file_08 == True:
            with open(filepath08, "rb") as f:
                mb08 = MIMEApplication(f.read())
            mb08.add_header("Content-Disposition", "attachment", filename=filename08)
            msg.attach(mb08)
        if file_09 == True:
            with open(filepath09, "rb") as f:
                mb09 = MIMEApplication(f.read())
            mb09.add_header("Content-Disposition", "attachment", filename=filename09)
            msg.attach(mb09)
        if file_10 == True:
            with open(filepath10, "rb") as f:
                mb10 = MIMEApplication(f.read())
            mb10.add_header("Content-Disposition", "attachment", filename=filename10)
            msg.attach(mb10)
        if file_11 == True:
            with open(filepath11, "rb") as f:
                mb11 = MIMEApplication(f.read())
            mb11.add_header("Content-Disposition", "attachment", filename=filename11)
            msg.attach(mb11)
        if file_12 == True:
            with open(filepath12, "rb") as f:
                mb12 = MIMEApplication(f.read())
            mb12.add_header("Content-Disposition", "attachment", filename=filename12)
            msg.attach(mb12)

        #メールを送付
        s = smtplib.SMTP(smtp_server, smtp_port)
        s.starttls()
        s.login(smtp_user, smtp_password)
        s.sendmail(from_address, to_address, msg.as_string())
        s.quit()

        st.write("Transmission completed !")