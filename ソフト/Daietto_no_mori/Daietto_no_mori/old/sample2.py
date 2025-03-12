import streamlit as st

# アプリケーションのタイトル
st.title('')

# テキスト入力欄
post_content = st.text_input('あなたの投稿を入力してください:')

# 投稿ボタン
st.button('投稿する')