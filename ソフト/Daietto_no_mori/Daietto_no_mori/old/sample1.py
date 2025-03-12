import requests
from PIL import Image
import numpy as np
import tensorflow as tf

# TensorFlowの事前訓練済みモデルを使用（例：MobileNetV2）
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# 食材を認識する関数
def recognize_food(image_path):
    image = Image.open(image_path).resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    preds = model.predict(image)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=5)
    
    # 予測結果を表示（上位5つを出力）
    for i, (code, name, score) in enumerate(decoded_preds[0]):
        print(f"{i+1}. {name}: {score * 100:.2f}%")

    # ここで食材名（name）を返す
    return decoded_preds[0][0][1]

# カロリーを取得する関数（ダミーAPI）
def get_calories(food_name):
    # 例: 食材名を基に栄養データベースからカロリー情報を取得
    # APIやローカルデータベースを使う
    # 仮のデータを返す
    calorie_database = {
        "apple": 52,
        "banana": 89,
        "pizza": 266,
    }
    
    return calorie_database.get(food_name.lower(), "カロリー情報が見つかりません")

# メイン処理
image_path = 'food_image.jpg'  # ここに画像ファイルのパスを指定
food_name = recognize_food(image_path)
print(f"認識された食材: {food_name}")

calories = get_calories(food_name)
print(f"推定カロリー: {calories} kcal")
