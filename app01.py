import streamlit as st
import sqlite3
import hashlib

s=st.secrets["PASSWORD"]

#LoginPassをしまうLBboxを作る
conn = sqlite3.connect('LPBox.db')
c = conn.cursor()

#LoginPassはハッシュを通して記録する
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def main():
    st.title("SlimeFarm SampleSite")
    username = st.sidebar.text_input("id")
    password = st.sidebar.text_input("password",type='password')
    if st.sidebar.checkbox("login"):
        create_user()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.sidebar.success("{}さんでログインしました".format(username))
            
        else:
            st.sidebar.warning("ユーザー名かパスワードが間違っています")
    
    #elif choice == "サインアップ":
        #st.subheader("新しいアカウントを作成します")
        #new_user = st.text_input("ユーザー名を入力してください")
        #new_password = st.text_input("パスワードを入力してください",type='password')

        #if st.button("サインアップ"):
            #create_user()
            #add_user(new_user,make_hashes(new_password))
            #st.success("アカウントの作成に成功しました")
            #st.info("ログイン画面からログインしてください")
if __name__ == '__main__':
        main()