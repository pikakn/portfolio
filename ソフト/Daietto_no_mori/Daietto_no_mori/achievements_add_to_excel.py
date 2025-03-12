import pandas as pd
from datetime import datetime

file_path = 'datafile/home_data.xlsx'  # 既存のExcelファイルのパス

def add_achievements(new_achievements):
    df = pd.read_excel(file_path)
    new_date = datetime.now().strftime('%m.%d').lstrip('0').replace('.0', '/')  # 例: 10.1

    # 新しいデータを追加
    new_data = {'日付': new_date, '返済実績': new_achievements}

    df['日付'] = df['日付'].astype(str)
    if new_date in df['日付'].values:
        # 同じ日付がある場合は、その行の体重を上書き
        df.loc[df['日付'] == new_date, '返済実績'] = new_achievements
        print(f"既存の日付 {new_date} の実績を {new_achievements} に上書きしました。")
    else:
        # 同じ日付がない場合は、新しい行として追加
        df = df._append(new_data, ignore_index=True)
        print(f"新しい日付 {new_date} と実績 {new_achievements} を追加しました。")

    # Excelファイルに上書き保存
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer :
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    print(f"新しい実績データが追加され、{file_path}に保存されました。")