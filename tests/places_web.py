import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://divar.ir/",
    "Origin": "https://divar.ir",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Connection": "keep-alive",
}

response = requests.get("https://map.divarcdn.com/places-web.json", headers=headers)
print(response.headers)
print(response.status_code)
print(response.text)
print(response.json())
