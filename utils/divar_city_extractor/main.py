import json
import os
import time

import requests


class DivarScraper:
    def __init__(self, output_folder="divar_data"):
        self.output_folder = output_folder
        # ایجاد پوشه اگر وجود نداشته باشد
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"پوشه {self.output_folder} ساخته شد.")

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0",
            "Referer": "https://divar.ir/",
            "Origin": "https://divar.ir",
        }
        self.api_url = "https://api.divar.ir/v8/w/lazy-multi-select-hierarchy-options"

    def save_data(self, filename, data):
        # آدرس کامل فایل: پوشه + اسم فایل
        file_path = os.path.join(self.output_folder, f"{filename}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"ذخیره شد: {file_path}")

    # بقیه متدها مثل قبل...
    def get_districts(self, city_id):
        payload = {
            "payload": {
                "@type": "type.googleapis.com/post_list.LazyFilterPayload",
                "filter_name": "districts",
                "version": "80",
                "place_ids": [str(city_id)],
            }
        }
        try:
            response = requests.post(
                self.api_url, headers=self.headers, json=payload, timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching {city_id}: {e}")
            return None

    def run_process(self, city_file):
        with open(city_file, "r", encoding="utf-8") as f:
            cities = json.load(f)

        for city in cities:
            print(f"Fetching {city['slug']}...")
            data = self.get_districts(city["id"])
            if data:
                self.save_data(city["slug"], data)
                time.sleep(1)

            # اجرای کد


scraper = DivarScraper(output_folder="City&Districts-id")
scraper.run_process("supplies\city.json")
