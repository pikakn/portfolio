class person:
    def __init__(self,name,age,sex,height,weight,object_gram):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
class diet:
    def __init__(self,name,user,food,exercise,calorie):
        self.name = name
        self.user = user
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    def add_calorie(self,foodname):
        self.calorie += foodname.calorie
    
    def exercise(self,)
    
    
        
print("Let's begin with filling your data,name,age,sex,height,weight,and object_gram.")
you_user = person(input(),input(),input(),input(),input(),input())
you = diet(you_user.name,1,0,0,0) 
print("you begin the diet!")       

#主食
rice = diet("ごはん",0,1,0,336)
rice = diet("食パン1枚",0,1,0,177)
rice = diet("うどん",0,1,0,311)
#副菜
rice = diet("サラダ",0,1,0,81)
rice = diet("味噌汁",0,1,0,33)
#主菜
rice = diet("卵焼き",0,1,0,142)
rice = diet("納豆",0,1,0,200)
rice = diet("焼き魚(鮭)",0,1,0,118)
rice = diet("ハンバーグ",0,1,0,437)
#牛乳・乳製品
rice = diet("牛乳200ml",0,1,0,134)
rice = diet("ヨーグルト1パック",0,1,0,62)
#果物
rice = diet("みかん",0,1,0,34)
apple = diet("りんご",0,1,0,135)

print(apple.calorie)
