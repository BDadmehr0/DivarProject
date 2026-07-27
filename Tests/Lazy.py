import requests

cookies = {
    'multi-city': 'tehran',
    'city': 'tehran',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'Referer': 'https://divar.ir/',
    'X-Screen-Size': '1724x1057',
    'traceparent': '00-3524e13a1ac1b3df71f614c5840c5507-0dd865a378257f47-00',
    'tracestate': 'sentry.sampled_not_recording=1,sentry.sample_rand=0.06852931022852937,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/w/lazy-multi-select-hierarchy-options',
    'sentry-trace': '3524e13a1ac1b3df71f614c5840c5507-0dd865a378257f47-0',
    'baggage': 'sentry-environment=client,sentry-release=the-wall-v14-14-0,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=3524e13a1ac1b3df71f614c5840c5507,sentry-sampled=false,sentry-sample_rand=0.06852931022852937,sentry-sample_rate=0.01',
    'Origin': 'https://divar.ir',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Connection': 'keep-alive',
    # 'Cookie': 'did=b030689c-3d42-4a2e-a811-883e88c9c422; cdid=ac500cf5-e04b-4cb9-aa5b-d86d098e1db9; ff=%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1784929742578%2C%22r%22%3A1785012542578%7D; multi-city=mashhad%7C; city=mashhad; csid=; theme=dark; sFrontToken=; _vid_t=lI1kh4kmMZhOyWQWs5Fw940BZEuBPpZNgPMyHwXE89D4qPy6UgTxYSEpIHkM4ambqBrx6eIOvj2qHg==; token=',
}

json_data = {
    'payload': {
        '@type': 'type.googleapis.com/post_list.LazyFilterPayload',
        'filter_name': 'districts',
        'version': '80',
        'place_ids': [
            '1',
        ],
    },
}

response = requests.post(
    'https://api.divar.ir/v8/w/lazy-multi-select-hierarchy-options',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)
print(response.status_code)
print(response.json())
print(response.headers)