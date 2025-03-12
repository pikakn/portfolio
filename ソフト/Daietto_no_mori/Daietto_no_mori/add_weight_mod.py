import streamlit as st
import weight_add_to_excel

def add_weight_page():
    st.title('体重測定')
    new_weight = st.number_input('', min_value=20.0, max_value=1000.0, value=None, step=1.0)
    #保存ボタン
    save_button = st.button('保存する')
    if save_button:
        if new_weight == None:
            st.error('体重を入力してください。')
        else:
            weight_add_to_excel.add_weight(new_weight)

    if st.button('ホームに戻る'):
        st.session_state['page'] = 'home'  # ホームに戻る
        st.rerun()