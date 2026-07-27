import requests
import os


path = "C:/Users/ASUS/Desktop/DivarPrj/src/supplies/Links.txt"
with open(path, "r") as f:
    url = f.read().strip().split("\n")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Content-Type": "application/json",
    "Referer": "https://divar.ir/",
    "X-Screen-Size": "1542x1057",
    "X-Standard-Divar-Error": "true",
    "X-Render-Type": "CSR",
    "Origin": "https://divar.ir",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Connection": "keep-alive",
    # 'Cookie': 'did=b030689c-3d42-4a2e-a811-883e88c9c422; cdid=ac500cf5-e04b-4cb9-aa5b-d86d098e1db9; multi-city=tehran%7C; city=tehran; csid=; theme=dark; sFrontToken=; _vid_t=lI1kh4kmMZhOyWQWs5Fw940BZEuBPpZNgPMyHwXE89D4qPy6UgTxYSEpIHkM4ambqBrx6eIOvj2qHg==; token=; ff=%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1785071638199%2C%22r%22%3A1785154438199%7D; referrer=',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

cookies = {
    "did": "b030689c-3d42-4a2e-a811-883e88c9c422",
    "cdid": "ac500cf5-e04b-4cb9-aa5b-d86d098e1db9",
}

data = json_data = {
    "city_ids": [
        "1",
    ],
    "source_view": "FILTER",
    "pagination_data": {
        "@type": "type.googleapis.com/post_list.PaginationData",
        "last_post_date": "2026-07-19T07:33:18.867805Z",
        "page": 1,
        "layer_page": 1,
        "search_uid": "f0f77a84-b39b-4a30-93ae-8a378af0d905",
        "cumulative_widgets_count": 24,
        "viewed_tokens": "H4sIAAAAAAAE/xTO0U7CQBCF4RcaEiUF7KUoslYtcStb7Y052S2ntFHRuHTr05u5+zPJNzlElWfnuRciuM7YPyEOafq+WApRJbPcUojBDV99JUTfYfMxCtGG8bhyenHG+xvlp3I7vgpxnduXz0KI4zoFkwvRFbPYbzQWv3XUh225D6Uq5vE83wlBG2p/K8TersrhR2c0aZqpCk00Dwch3tbZ4+lJCF+83zmn0bT3zbOGzdJiJ4S/NP1V/R8AAP//mgMTP9cAAAA=",
        "search_bookmark_info": {
            "search_hash": "2f75084f377f618a8bb0f5bbe938f413",
            "bookmark_state": {},
            "alert_state": {},
        },
        "first_page_viewed_at": "2026-07-26T12:21:49.581884289Z",
    },
    "disable_recommendation": False,
    "map_state": {
        "camera_info": {
            "bbox": {},
        },
    },
    "search_data": {
        "form_data": {
            "data": {
                "districts": {
                    "repeated_string": {
                        "value": [
                            "992",
                        ],
                    },
                },
                "category": {
                    "str": {
                        "value": "residential-rent",
                    },
                },
            },
        },
        "server_payload": {
            "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
            "additional_form_data": {
                "data": {
                    "sort": {
                        "str": {
                            "value": "sort_date",
                        },
                    },
                },
            },
        },
    },
}

response = requests.post(url[1], json=data, headers=headers, cookies=cookies)
print(response.text)
print(response.json().get("pagination").get("data"))
