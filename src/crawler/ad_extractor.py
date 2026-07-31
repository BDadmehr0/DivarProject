import csv
import json
import os

import requests

from utils.cookies import get_cookies

CSV_FILE = "clean_ads.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
}

COOKIES = get_cookies()

agency_keywords = [
    # مستقیم
    "املاک",
    "مشاور املاک",
    "دفتر املاک",
    "بنگاه",
    "آژانس املاک",
    "آژانس",
    "کارشناس املاک",
    "کارشناس منطقه",
    "مشاور",
    "مشاورین",
    # عبارت‌های رایج مشاورها
    "فایل",
    "فایلینگ",
    "فایل ویژه",
    "فایل جدید",
    "فایل اکازیون",
    "فایل فروش",
    "فایل اجاره",
    # همکاری و تبلیغات بنگاهی
    "همکار تماس نگیرد",
    "همکار تماس نگیره",
    "همکاری با مشاور",
    "با مشاورین همکاری نمی‌شود",
    "بدون واسطه",
    "بدون واسطه نیست",
    # جملات رایج آگهی‌گذارها
    "جهت بازدید تماس",
    "جهت اطلاعات بیشتر تماس",
    "بازدید با هماهنگی",
    "برای بازدید تماس بگیرید",
    "مشاور فروش",
    "مشاور شما",
    # نام‌گذاری دفترها
    "گروه املاک",
    "مجموعه املاک",
    "تیم املاک",
    "دفتر معاملات",
    "معاملات ملکی",
    "کارگزاری",
    "دفتر ملکی",
    # شماره و معرفی کارشناس
    "کارشناس:",
    "مشاور:",
    "مدیر فروش",
    "مدیر منطقه",
    "جهت اطلاعات بیشتر و هماهنگی بازدید تماس بگیرید.",
    "موارد دیگر متناسب با بودجه شما",
]


def build_url(token, ad_instance_id):
    return f"https://api.divar.ir/v8/posts-v2/web/{token}?tracker_session_id={ad_instance_id}"


def fetch_json(url):
    response = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=20)
    response.raise_for_status()
    return response.json()


def extract_widgets(data):
    return data.get("list_widgets", [])


def extract_post_info(widget):
    payload = widget.get("data", {}).get("action", {}).get("payload", {})
    token = payload.get("token")
    ad_instance_id = payload.get("ad_instance_id")
    return token, ad_instance_id


def extract_text(ad_data):
    try:
        return ad_data["sections"][2]["widgets"][1]["data"]["text"]
    except (KeyError, IndexError, TypeError):
        return ""


def is_agency_text(text):
    return any(keyword in text for keyword in agency_keywords)


def save_to_csv(row):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, "a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["token", "ad_instance_id", "web_url", "text"])
        writer.writerow(row)


def main(response_file):
    with open(response_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    widgets = extract_widgets(data)

    for idx, widget in enumerate(widgets):
        token, ad_instance_id = extract_post_info(widget)

        if not token or not ad_instance_id:
            continue

        try:
            ad_data = fetch_json(build_url(token, ad_instance_id))
        except requests.RequestException as e:
            print(f"[{idx}] request failed: {e}")
            continue

        text = extract_text(ad_data)

        if is_agency_text(text):
            print(f"[{idx}] skipped as agency")
            continue

        web_url = ad_data.get("share", {}).get("web_url", "")
        save_to_csv([token, ad_instance_id, web_url, text])
        print(f"[{idx}] saved")


if __name__ == "__main__":
    main("response_1.json")
