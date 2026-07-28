import requests
import json
from pathlib import Path

# دریافت داده‌ها
url = 'https://s100.divarcdn.com/static/public/search/filters-config.json'
try:
    response = requests.get(url)
    response.raise_for_status()  # بررسی اینکه آیا درخواست موفق بوده یا خیر
    data = response.json()
except Exception as e:
    print(f"Error fetching data: {e}")
    exit()

# تعیین مسیر
p = Path(r'C:\Users\ASUS\Desktop\DivarProject-main\data\supplies\categories.json')

try:
    # ۱. ایجاد پوشه‌ها اگر وجود ندارند (parents=True تمام مسیر را می‌سازد)
    p.parent.mkdir(parents=True, exist_ok=True)

    # ۲. نوشتن فایل
    p.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    print(f"Successfully saved to: {p}")

except PermissionError:
    print("Error: Permission Denied. Try running your IDE/Terminal as Administrator.")
except Exception as e:
    print(f"An error occurred: {e}")    