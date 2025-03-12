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
    
    # 食べ物を食べる関数　calorieに食べ物のcalorieを代入
    def add_calorie(self,calorie):
        self.calorie += calorie

    # 運動をする関数　時間をトラッキングしweightにuserの体重、exerciseに運動のメッツ(calorie)を代入
    def exerciseGo(self,weight,exercise,duration):
        calorie = exercise*weight*duration*1.05
        self.calorie -= calorie
        return calorie

def add_ac_calories(new_weight):
    import pandas as pd
    from datetime import datetime

    file_path = 'datafile/home_data.xlsx'
    df = pd.read_excel(file_path)
    new_date = datetime.now().strftime('%m.%d').lstrip('0').replace('.0', '/')  # 例: 10.1

    # 新しいデータを追加
    new_data = {'日付': new_date, "返済実績":-new_weight,'累計カロリー': new_weight}

    # DataFrameに新しい行を追加
    #df = df._append(new_data, ignore_index=True)
    df['日付'] = df['日付'].astype(str)
    if new_date in df['日付'].values:
        # 同じ日付がある場合は、その行の体重を上書き
        df.loc[df['日付'] == new_date, '累計カロリー'] = new_weight
        df.loc[df['日付'] == new_date, '返済実績'] = new_weight
        print(f"既存の日付 {new_date} の累計カロリーを {new_weight} に上書きしました。")
    else:
        # 同じ日付がない場合は、新しい行として追加
        df = df._append(new_data, ignore_index=True)
        print(f"新しい日付 {new_date} と累計カロリー {new_weight} を追加しました。")

    # Excelファイルに上書き保存
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer :
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    print(f"新しい累計カロリーデータが追加され、{file_path}に保存されました。")    

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

nothing = diet("",0,1,0,0)
rice = diet("ごはん",0,1,0,336)
bread = diet("食パン1枚",0,1,0,177)
udon = diet("うどん",0,1,0,311)
#副菜
salad = diet("サラダ",0,1,0,81)
misosoup = diet("味噌汁",0,1,0,33)
#主菜
japomlett = diet("卵焼き",0,1,0,142)
natto = diet("納豆",0,1,0,200)
friedfish = diet("焼き魚(鮭)",0,1,0,118)
hamberg = diet("ハンバーグ",0,1,0,437)
#牛乳・乳製品
milk = diet("牛乳200ml",0,1,0,134)
yorgurt = diet("ヨーグルト1パック",0,1,0,62)
#果物
orenge = diet("みかん",0,1,0,34)
apple = diet("りんご",0,1,0,135)    
        

you_user = person("John",2,"male",173,63,3,1)
you = diet(you_user.user,1,0,0,0) 