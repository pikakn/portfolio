#運動の入力
class person:
    def __init__(self,user,age,sex,height,weight,object_gram):
        self.user = user
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
        

class diet:
    def __init__(self,name,usern,food,exercise,calorie):
        self.name = name
        self.usern = usern
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    def add_calorie(self,calorie):
        self.calorie += calorie

    def exerciseGo(self,weight,exercise,duration):
        calorie = exercise*weight*duration*1.05
        self.calorie -= calorie
        return calorie 
    

#消費カロリー(kcal) ＝ メッツ × 体重(kg)×運動時間(分) ×1.05
#運動の消費カロリー
cycling = diet("自転車", 0, 0, 1, 4)
walking = diet("ウォーキング", 0, 0, 1, 3)
running = diet("ランニング", 0, 0, 1, 7)
dance = diet("ダンス", 0, 0, 1, 4)
swimming = diet("水泳", 0, 0, 1, 5)
weak_strength_training = diet("筋トレ(低強度)", 0, 0, 1, 4)
strong_strength_training = diet("筋トレ(高強度)", 0, 0, 1, 8)
yoga = diet("ヨガ", 0, 0, 1, 2.5)
trekking = diet("登山", 0, 0, 1, 5)
weak_sports = diet("スポーツ", 0, 0, 1, 4)
strong_sports = diet("スポーツ(激しめ)", 0, 0, 1, 8)    


you_user = person("John",23,"male",175,63,2)
you = diet(you_user.user,1,0,0,0) 

import streamlit as st
import time
# 運動の種類を選択するセレクトボックスを作成
exercise_options_names = [
    walking,running,cycling,yoga,trekking,dance,swimming,   
    strong_strength_training,weak_strength_training,weak_sports,strong_sports]
exercise_options =[
    "ウォーキング", "ランニング", "自転車", "ヨガ", "登山", "ダンス", "水泳",
    "筋トレ（高強度）", "筋トレ（低強度）", "スポーツ", "スポーツ（激しめ）"
]
# タイトルと運動の種類選択

def exercise():
    st.title("運動のトラッキングアプリ")
    exercise_name = st.selectbox("運動の種類を選んでください:", exercise_options)
    for i in range(len(exercise_options)):
        if exercise_name == exercise_options[i]:
            exercise = exercise_options_names[i]
    # 運動開始とストップのボタン
    start_button = st.button("運動開始！")
    stop_button = st.button("ストップ")
    # 運動の開始時間を保持する変数
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    # 経過時間を表示する変数
    if "elapsed_time" not in st.session_state:
        st.session_state.elapsed_time = 0
    # 開始ボタンが押されたときの処理
    if start_button:
        st.session_state.start_time = time.time()  # 現在の時間を取得して保存
        st.session_state.elapsed_time = 0          # 経過時間をリセット
        st.write(f"【{exercise_name}】が開始されました！")
    # ストップボタンが押されたときの処理
    if stop_button and st.session_state.start_time is not None:
        duration = time.time() - st.session_state.start_time
        result = diet.exerciseGo(you,you_user.weight,exercise.calorie,duration)
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.start_time = None  # ストップしたので開始時間をリセット
        st.write(f"【{exercise_name}】が終了しました。")
        st.write(f"経過時間: {int(st.session_state.elapsed_time // 3600):02}:{int((st.session_state.elapsed_time % 3600) // 60):02}:{int(st.session_state.elapsed_time % 60):02}")
        st.write(f"{int(result)}カロリー消費しました。")
    # 運動中の経過時間を表示
    if st.session_state.start_time is not None:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.write(f"現在の経過時間: {int(st.session_state.elapsed_time // 3600):02}:{int((st.session_state.elapsed_time % 3600) // 60):02}:{int(st.session_state.elapsed_time % 60):02}")
    
    if st.button('ホームに戻る'):
        st.session_state['page'] = 'home'  # ホームに戻る
        
exercise()