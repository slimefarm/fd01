import streamlit as st
import sqlite3
import hashlib
import app02
import app99

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
    st.sidebar.subheader("Login Site")
    username = st.sidebar.text_input("username")
    password = st.sidebar.text_input("password",type='password')
    
    #if st.sidebar.checkbox("Login"): ←サンプルはチェックボックスがあったが削除
    create_user()
    hashed_pswd = make_hashes(password)

    result = login_user(username,check_hashes(password,hashed_pswd))
    if result:
        #PAGES = {"App2": app02,"App3": app03}
        PAGES = {"Send Gmail": app02,"Configuration":app99}
        st.sidebar.subheader('Navi Site')
        selection = st.sidebar.selectbox("menu",PAGES)
        page = PAGES[selection]
        page.app()
        
    else:
        st.sidebar.info("*Hi ! pls input username & password !*")

if __name__ == '__main__':
        main()