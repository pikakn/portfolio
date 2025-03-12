#exerciseページの内容
import streamlit as st
import time

class person:
    def __init__(self,user,age,sex,height,weight,object_gram,week_terget):
        self.user = user
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
        self.weight_history = week_terget
        
    def update_weight(self, new_weight):
        self.weight = new_weight
        self.weight_history.append(new_weight)  # 体重を履歴に保存
        

class diet:
    def __init__(self,name,usern,food,exercise,calorie):
        self.name = name
        self.usern = usern
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    # 食べ物を食べる関数　calorieに食べ物のcalorieを代入
    def add_calorie(self,calorie):
        self.calorie += calorie

    # 運動をする関数　時間をトラッキングしweightにuserの体重、exerciseに運動のメッツ(calorie)を代入
    def exerciseGo(self,weight,exercise,duration):
        calorie = exercise*weight*duration*1.05
        self.calorie -= calorie
        return calorie 
        
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
        
you_user = person("John",23,"male",175,63,3,[65])
you = diet(you_user.user,1,0,0,0) 

def exercise_page():
    # 運動の種類を選択するセレクトボックスを作成
    exercise_options =[
    "ウォーキング", "ランニング", "自転車", "ヨガ", "登山", "ダンス", "水泳",
    "筋トレ（高強度）", "筋トレ（低強度）", "スポーツ", "スポーツ（激しめ）"
    ]
    # タイトルと運動の種類選択
    st.title('運動')
    exercise = st.selectbox(
        '運動の種類を選んでください:',
        exercise_options,
        format_func=lambda diet: diet.name
    )
    exercise_mets = exercise.calorie
    # タイマー表示用のプレースホルダを作成
    timer_placeholder = st.empty()
    # 運動開始とストップのボタン
    start_button = st.button('運動開始！')
    stop_button = st.button('ストップ')
    # 運動の開始時間を保持する変数
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    # 経過時間を表示する変数
    if 'elapsed_time' not in st.session_state:
        st.session_state.elapsed_time = 0
    # 開始ボタンが押されたときの処理
    if start_button:
        st.session_state.start_time = time.time()  # 現在の時間を取得して保存
        st.session_state.elapsed_time = 0          # 経過時間をリセット
    # タイマーを動かす処理
    if st.session_state.start_time is not None:
        # 経過時間を更新しながら表示
        while not stop_button:
            st.session_state.elapsed_time = time.time() - st.session_state.start_time
            # 経過時間を「時:分:秒」の形式で表示
            timer_placeholder.write(
                f"{int(st.session_state.elapsed_time // 3600):02}:"
                f"{int((st.session_state.elapsed_time % 3600) // 60):02}:"
                f"{int(st.session_state.elapsed_time % 60):02}"
            )
            # 1 秒のスリープを挟んで再描画
            time.sleep(1)
    # ストップボタンが押されたときの処理
    if stop_button and st.session_state.start_time is not None:
        timer_placeholder.write(
            f"{int(st.session_state.elapsed_time // 3600):02}:"
            f"{int((st.session_state.elapsed_time % 3600) // 60):02}:"
            f"{int(st.session_state.elapsed_time % 60):02}"
        )
        st.session_state.elapsed_time=st.session_state.elapsed_time/360
        st.session_state.start_time = None  # ストップしたので開始時間をリセット
        st.write(diet.exerciseGo(you,you_user.weight,exercise_mets,st.session_state.elapsed_time))
    # 戻るボタンを追加して、exercise_page()を非表示にする
    if st.button('戻る'):
        st.session_state.show_exercise = False
        st.rerun()
        
exercise_page()