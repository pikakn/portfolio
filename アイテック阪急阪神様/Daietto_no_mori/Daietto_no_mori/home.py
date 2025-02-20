import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

import gemini_api
import exercise_mod
import food_mod
import add_weight_mod
import ac_calories_extraction_from_excel

class person:
    def __init__(self,user,age,sex,height,weight,object_gram,week_target):
        self.user = user
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
        self.week_target = week_target
        

class diet:
    def __init__(self,name,usern,food,exercise,calorie):
        self.name = name
        self.usern = usern
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
        
you_user = person("John",23,"male",175,63,[63],700)
you = diet(you_user.user,1,0,0,0)


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
st.image(image, width=600)
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
    if y == '返済実績':
        weight_data = df[y].dropna().tail(7)
    else:
        weight_data = df[y].dropna()

    plt.rcParams["font.size"] = 30
    plt.figure(figsize=(8, 5))
    plt.plot(weight_data.index, weight_data.values, marker='o', linestyle = '-')
    plt.title(y + 'の推移')
    #plt.xlabel('日付')
    plt.ylabel(y)
    plt.xticks(rotation=45)  # x軸のラベルを45度回転
    #plt.grid()

    # Streamlitにグラフを表示
    st.pyplot(plt)

def one_word_fromAi(filename, col):
    df = pd.read_excel(filename)
    list_data = df[col].values
    str_data = ", ".join(map(str,list_data))
    pronpt = '次の数値は体重の推移です。語尾は「だなも」で、nanを除いた時、減少していれば褒め、増加していれば慰めてください。1文でやさしくアドバイスしてください。' + str_data
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
            st.rerun()

    with col2:
        if st.button('運動'):
            st.session_state['page'] = 'exercise'
            st.rerun()

    with col3:
        if st.button('体重測定'):
            st.session_state['page'] = 'weight_measurement'
            st.rerun()

    # グラフ表示エリアのボックス
    progress_col1, progress_col2, progress_col3 = st.columns(3)

    with progress_col1:
        graph('datafile/home_data.xlsx', '日付', '体重')

    with progress_col2:
        graph('datafile/home_data.xlsx', '日付', '返済実績')

    with progress_col3: 
        st.text("今週のノルマ")
        left = int(you_user.week_target + ac_calories_extraction_from_excel.return_oneweek_ac_calories())
        st.text(f"残り: {left}マイル")
        
        rate = left/you_user.week_target      
        print(rate)
        if rate>1:
            st.text('｡°(°´ᯅ`°)°｡')
        elif rate>0.8:
            st.text('(-.-;)')
        elif rate>0.5:
            st.text('( .. )')
        elif rate>0.2:
            st.text('(￣∀￣)')
        elif rate>0.1:
            st.text('(^^)')
        elif rate>0:
            st.text('\(^^)/')


    one_word_fromAi('datafile/home_data.xlsx', '体重')

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'food':
    food_mod.food()
elif st.session_state.page == 'exercise':
    exercise_mod.exercise_page()
elif st.session_state.page == 'weight_measurement':
    add_weight_mod.add_weight_page()