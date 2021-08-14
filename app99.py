import streamlit as st
import sqlite3
import hashlib
import app01

def app():

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

    st.subheader("Create a new account")
    new_user = st.text_input("pls input username !")
    new_password = st.text_input("pls input password !",type='password')

    if st.button("Sign up"):
        create_user()
        add_user(new_user,make_hashes(new_password))
        st.success("Completed creating a new account !")