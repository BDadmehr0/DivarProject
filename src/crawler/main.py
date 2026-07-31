import json
import time

import requests

from utils.cookies import get_cookies

COOKIES = get_cookies()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Content-Type": "application/json",
    "Referer": "https://divar.ir/",
    "X-Screen-Size": "1101x807",
    "X-Standard-Divar-Error": "true",
    "X-Render-Type": "CSR",
    "traceparent": "00-57ad3a79e0d5bc72c47893ee329381a7-800f03019ffc7146-00",
    "tracestate": "sentry.sampled_not_recording=1,sentry.sample_rand=0.45178048310798347,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/search",
    "sentry-trace": "57ad3a79e0d5bc72c47893ee329381a7-800f03019ffc7146-0",
    "baggage": "sentry-environment=client,sentry-release=the-wall-v14-16-4,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=57ad3a79e0d5bc72c47893ee329381a7,sentry-sampled=false,sentry-sample_rand=0.45178048310798347,sentry-sample_rate=0.01",
    "Origin": "https://divar.ir",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Connection": "keep-alive",
    # 'Cookie': 'did=b030689c-3d42-4a2e-a811-883e88c9c422; cdid=ac500cf5-e04b-4cb9-aa5b-d86d098e1db9; multi-city=tehran%7C; city=tehran; csid=; theme=dark; sFrontToken=; _vid_t=lI1kh4kmMZhOyWQWs5Fw940BZEuBPpZNgPMyHwXE89D4qPy6UgTxYSEpIHkM4ambqBrx6eIOvj2qHg==; token=; referrer=; ff=%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1785206743985%2C%22r%22%3A1785289543985%7D',
}


# تنظیمات ثابت (فیلترها) - این بخش ثابت می‌ماند
SEARCH_FILTERS = {
    "form_data": {
        "data": {
            "warehouse": {"boolean": {"value": True}},
            "category": {"str": {"value": "apartment-rent"}},
            "balcony": {"boolean": {"value": True}},
            "elevator": {"boolean": {"value": True}},
            "parking": {"boolean": {"value": True}},
            "districts": {
                "repeated_string": {
                    "value": [
                        "178",
                        "4148",
                        "4177",
                    ],
                },
            },
        },
    },
    "server_payload": {
        "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
        "additional_form_data": {"data": {"sort": {"str": {"value": "sort_date"}}}},
    },
}


def get_response(pagination_payload):
    """ارسال درخواست به دیوار و بازگرداندن JSON"""
    json_data = {
        "city_ids": ["1"],
        "pagination_data": pagination_payload,
        "disable_recommendation": False,
        "map_state": {"camera_info": {"bbox": {}}},
        "search_data": SEARCH_FILTERS,
    }

    # نکته: حتما headers و cookies را قبلاً تعریف کرده باشید
    try:
        response = requests.post(
            "https://api.divar.ir/v8/postlist/w/search",
            headers=headers,
            json=json_data,
            cookies=COOKIES,
            timeout=10,
        )
        return response.json()
    except Exception as e:
        print(f"خطا در درخواست: {e}")
        return None


def save_to_file(filename, data):
    """ذخیره داده‌ها در فایل JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# --- شروع عملیات ---

# --- شروع عملیات اصلاح شده ---

print("در حال دریافت صفحه اول...")
first_res = get_response(None)

if first_res:
    save_to_file("response_1.json", first_res)
    print("صفحه اول ذخیره شد.")

    # استخراج مسیر درست بر اساس لاگ شما
    # مسیر: action_log -> server_side_info -> info
    info_layer = (
        first_res.get("action_log", {}).get("server_side_info", {}).get("info", {})
    )

    # استخراج Pagination Data (اگر در لایه info نیست، باید در جای دیگری از پاسخ جستجو شود)
    # معمولاً در دیوار، pagination_data در همان لایه info یا کنار آن است
    pagination_data = first_res.get("pagination", {}).get("data")

    # گرفتن وضعیت صفحه بعدی از مسیر صحیح که در لاگ شما بود
    has_next = info_layer.get("has_next_page", False)

    counter = 2
    while has_next and pagination_data:
        print(f"در حال دریافت صفحه {counter}...")

        current_res = get_response(pagination_data)

        if current_res:
            save_to_file(f"response_{counter}.json", current_res)
            print(f"صفحه {counter} ذخیره شد.")

            # آپدیت کردن لایه اطلاعات برای چک کردن has_next_page در مرحله بعد
            new_info_layer = (
                current_res.get("action_log", {})
                .get("server_side_info", {})
                .get("info", {})
            )

            # آپدیت کردن داده‌های پیمایش
            pagination_data = current_res.get("pagination", {}).get("data")

            # آپدیت کردن وضعیت صفحه بعدی از مسیر صحیح
            has_next = new_info_layer.get("has_next_page", False)

            time.sleep(2)
            counter += 1
        else:
            print("خطا در دریافت داده.")
            break
else:
    print("عدم موفقیت در دریافت صفحه اول.")
