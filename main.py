import random
import datetime

numbers = random.sample(range(1, 40), 5)
numbers.sort()

formatted_numbers = [f"{n:02d}" for n in numbers]
result_string = ", ".join(formatted_numbers)

update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>佾儒算明牌，今彩539預測(測試中)</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background-color: #f0f2f5; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
        .numbers {{ font-size: 24px; color: #d9534f; font-weight: bold; margin: 20px 0; }}
        .footer {{ color: #888; font-size: 12px; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>佾儒算明牌，今彩539預測</h1>
        <p>今日號碼：</p>
        <div class="numbers">{result_string}</div>
        <p>更新時間 (UTC): {update_time}</p>
        <div class="footer">小時候都被阿仁問明牌，長大學AI寫程式乾脆來算算看，本網站目前為測試階段，數字為隨機生成，僅供開發測試。</div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("網頁更新完成！")
