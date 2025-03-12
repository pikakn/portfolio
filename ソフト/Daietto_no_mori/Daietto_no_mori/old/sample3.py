import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import sys

import gemini_api
import old.exercise_mod_old1 as exercise_mod_old1
import old.exercise_old3 as exercise_old3
import food_mod
import add_weight_mod


image = Image.open('datafile/daietto_no_mori.png')
st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 画像を表示
st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image(image, width=400)
st.markdown('</div>', unsafe_allow_html=True)


button_css = """
<style>
    button {
        width: 200px;
        height: 150px;
        border-radius: 10px; /* 枠線：半径10ピクセルの角丸 */
        background: #C57038; /* 背景色：薄いグレー */
        color: white; /* 文字色 */
        border: none; /* 枠線なし */
        font-size: 18px; /* フォントサイズ */
    }
</style>
"""



def graph(filename, x, y):
    df = pd.read_excel(filename, index_col=x)
    weight_data = df[y].dropna()

    plt.figure(figsize=(8, 5))
    plt.plot(weight_data.index, weight_data.values, marker='o', linestyle = '-')
    plt.title('体重の推移')
    plt.xlabel('日付')
    plt.ylabel(y)
    plt.xticks(rotation=45)  # x軸のラベルを45度回転
    plt.grid()

    # Streamlitにグラフを表示
    st.pyplot(plt)

def one_word_fromAi(filename, col):
    df = pd.read_excel(filename)
    list_data = df[col].values
    str_data = ", ".join(map(str,list_data))
    pronpt = '次の数値は体重の推移です。nanを除いた時、減少していれば褒め、増加していれば慰めてください。1文でやさしくアドバイスしてください。' + str_data
    #print(pronpt)
    st.text(gemini_api.ask_gemini(pronpt))

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def home():
# レイアウトのためのカラム
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("食事"):
            st.session_state['page'] = 'food'

    with col2:
        if st.button('運動'):
            st.session_state['page'] = 'exercise'

    with col3:
        if st.button('体重測定'):
            st.session_state['page'] = 'weight_measurement'

    # グラフ表示エリアのボックス
    progress_col1, progress_col2, progress_col3 = st.columns(3)

    with progress_col1:
        graph('datafile/home_data.xlsx', '日付', '体重')

    with progress_col2:
        graph('datafile/home_data.xlsx', '日付', '返済実績')

    with progress_col3:
        st.text("今週のノルマ")
        st.text("残り: 50%")  # 残り部分など動的な数値を表示


    one_word_fromAi('datafile/home_data.xlsx', '体重')

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'food':
    food_mod.food()
elif st.session_state.page == 'exercise':
    #exercise_mod.exercise()
    exercise_old3.exercise_page()
elif st.session_state.page == 'weight_measurement':
    add_weight_mod.add_weight_page()