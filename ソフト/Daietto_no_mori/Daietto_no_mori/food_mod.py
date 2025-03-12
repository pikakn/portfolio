import database_food as dataf

import streamlit as st
import pandas as pd
import datetime
import ac_calories_extraction_from_excel

def food():
    st.title("食事　摂取カロリー")
    you_user = dataf.person("John",23,"male",175,63,3,[65])
    you = dataf.diet(you_user.user,1,0,0,0)
    you.calorie = ac_calories_extraction_from_excel.return_oneweek_ac_calories()


    cerbo_options = [dataf.nothing,dataf.rice,dataf.bread,dataf.udon]
    mainmeal_options = [dataf.nothing,dataf.japomlett,dataf.natto,dataf.friedfish,dataf.hamberg]
    submeal_options = [dataf.nothing,dataf.salad,dataf.misosoup]
    sidemenu_options = [dataf.nothing,dataf.milk,dataf.yorgurt,dataf.orenge,dataf.apple]

    cerbo = st.selectbox("主食の種類を選んでください:", cerbo_options,format_func=lambda x:x.name)
    mainmeal = st.selectbox("主菜の種類を選んでください", mainmeal_options,format_func=lambda x:x.name)
    submeal = st.selectbox("副菜の種類を選んでください", submeal_options,format_func=lambda x:x.name)
    sidemenu = st.selectbox("サイドメニューの種類を選んでください",sidemenu_options,format_func=lambda x:x.name)

    # 表示
    df2 = pd.DataFrame({
            "日時":"表示サンプル",
            "主食":"",
            "主菜":"",
            "副菜":"",
            "サイドメニュー":"",
            "カロリー":"0"
            },index=[0])
    # session_state でボタンによる入力を保持 辞書の形式で格納している
    if "eatlist" not in st.session_state:
        st.session_state.eatlist = [df2]
    st.write("lets eat!")


    if st.button("食べる"): #食べたもののリストが累積していく　データベースとの照合はあと
        datenow = datetime.datetime.now()
        date = "{}/{}/{}".format(datenow.year,datenow.month,datenow.day)
        calorie_menu = cerbo.calorie + mainmeal.calorie + submeal.calorie + sidemenu.calorie
        calorie_menu = str(calorie_menu)
        dfnow = pd.DataFrame({
            "日時":date,
            "主食":cerbo.name,
            "主菜":mainmeal.name,
            "副菜":submeal.name,
            "サイドメニュー":sidemenu.name,
            "カロリー":calorie_menu
            },index=[0])
        st.session_state.eatlist.append(dfnow)    
    df2 = pd.concat(st.session_state.eatlist)
    st.write(df2) 

    sum_calorie_menu = 0
    for i in st.session_state.eatlist:
        sum_calorie_menu += int(i.iat[0,5])

    meal_eatnow = st.session_state.eatlist[-1].iat[0,5]
    st.write(f"{meal_eatnow}カロリーの摂取だ")

    dataf.diet.add_calorie(you,sum_calorie_menu)
    dataf.add_ac_calories(you.calorie)

    # データyouに情報を更新
    st.write(f"今のカロリーは{you.calorie}だ！")
        
    if st.button('ホームに戻る'):
        st.session_state['page'] = 'home'  # ホームに戻る
        st.rerun()