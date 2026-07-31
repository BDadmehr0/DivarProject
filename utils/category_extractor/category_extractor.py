import json
import requests
import time
import os
from field_extractor import FieldExtractor

extract = FieldExtractor()

directory_name = 'Divar_filters'
cookies = {
    'did': '7593062c-bc1c-4fb2-980c-04f589d55d62',
    'cdid': '5bb7e4f6-17ef-4074-8a46-29a87912a805',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=client,sentry-release=the-wall-v14-24-2,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=301d55ec1180ff6d1f7bb8b78b92d2cd,sentry-sampled=false,sentry-sample_rand=0.45049157043364196,sentry-sample_rate=0.01',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://divar.ir',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://divar.ir/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sentry-trace': '301d55ec1180ff6d1f7bb8b78b92d2cd-15e49537629a5a19-0',
    'traceparent': '00-301d55ec1180ff6d1f7bb8b78b92d2cd-15e49537629a5a19-00',
    'tracestate': 'sentry.sampled_not_recording=1,sentry.sample_rand=0.45049157043364196,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/filters',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-render-type': 'CSR',
    'x-screen-size': '955x869',
    'x-standard-divar-error': 'true',
    # 'cookie': 'did=7593062c-bc1c-4fb2-980c-04f589d55d62; cdid=5bb7e4f6-17ef-4074-8a46-29a87912a805; multi-city=tehran%7C; city=tehran; theme=dark; _vid_t=rXcYTC0uvZ+dr6eUMD/J7UNBZ9E6TLA34oyJB25M1tWgsuAkuMuJ/e4/mIwHBtU/P/f731gogS9ozw==; referrer=; _ga=GA1.1.847434863.1784358426; _ga_CCSRPLKB4B=GS2.1.s1784358425$o1$g1$t1784358518$j27$l0$h0; token=; disable_map_view=true; csid=549f3266832dbeb656; sAccessToken=eyJraWQiOiJkLTE3ODUwNjM0NjI2NTEiLCJ0eXAiOiJKV1QiLCJ2ZXJzaW9uIjoiNCIsImFsZyI6IlJTMjU2In0.eyJpYXQiOjE3ODU0NDgwNDIsImV4cCI6MTc4NTQ1ODg0Miwic3ViIjoiMjYyYjUzZmItMzVkMC00MzRhLWFjY2UtY2I1NTg5OTQ1MjNjIiwidElkIjoicHVibGljIiwic2Vzc2lvbkhhbmRsZSI6ImYzZjgzMzZiLTY0ZTEtNGY2Ni1iOGE4LWUyNmM3YWM0YzBiMCIsInJlZnJlc2hUb2tlbkhhc2gxIjoiMWFkNzY0MjM2YmJkODlhOTdhZDQ5ZWQ5NDA0NWQ1ZDgxNTBjZjE3MDA2NDZhNWI3NzRlYmMzZTA5Yzg3MzNiYiIsInBhcmVudFJlZnJlc2hUb2tlbkhhc2gxIjoiMTY0MGIxZWQzMzkwNmJhNWUwYmY2OWY1OWMxYmVkNjRmOWFmZjg2N2ZlZjM2NjAzMzdjZGNlYTI5ODI5YTEwMCIsImFudGlDc3JmVG9rZW4iOm51bGwsImlzcyI6Imh0dHBzOi8vYXBpLmRpdmFyLmlyL3Y4L2F1dGhlbnRpY2F0ZSIsInBob25lTnVtYmVyIjoiKzk4OTkzNDI2MjUwMiIsInN0LXBlcm0iOnsidCI6MTc4NTQ0ODA0MiwidiI6W119LCJzdC1yb2xlIjp7InQiOjE3ODU0NDgwNDIsInYiOltdfX0.gjOwqtC_qJynsiBB28mNBnx5FPDv9qwfibwxQ-qSQ-adyQfPR2qct-FzucNLD7tpClgtdFSwp91NB3I99PnKY1YliX9c4iMf5ioob3kZSmOA0GinUGYJW3XUz4EFJEJXprhJiue-vhsFVvYkCqe2zGa5178N5_b0DdhrwmQWeATjHRVbjdjWmmw7kHpVj6iw3vPGXIsFt4Mn35p9LP9-QMkzCRFohLB_y4xtbdmTQ8ADQkHN_vhAuKBEw9GnBC9wkwjQVaFs4FXgBO_un4xV_jaWg6nQtiQz4qDiSiaC1sA0McDfCPGd8gcWiuhhvZePzD0kBWwM1CcPxqaVSMLlhA; sFrontToken=eyJ1aWQiOiIyNjJiNTNmYi0zNWQwLTQzNGEtYWNjZS1jYjU1ODk5NDUyM2MiLCJhdGUiOjE3ODU0NTg4NDIwMDAsInVwIjp7ImFudGlDc3JmVG9rZW4iOm51bGwsImV4cCI6MTc4NTQ1ODg0MiwiaWF0IjoxNzg1NDQ4MDQyLCJpc3MiOiJodHRwczovL2FwaS5kaXZhci5pci92OC9hdXRoZW50aWNhdGUiLCJwYXJlbnRSZWZyZXNoVG9rZW5IYXNoMSI6IjE2NDBiMWVkMzM5MDZiYTVlMGJmNjlmNTljMWJlZDY0ZjlhZmY4NjdmZWYzNjYwMzM3Y2RjZWEyOTgyOWExMDAiLCJwaG9uZU51bWJlciI6Iis5ODk5MzQyNjI1MDIiLCJyZWZyZXNoVG9rZW5IYXNoMSI6IjFhZDc2NDIzNmJiZDg5YTk3YWQ0OWVkOTQwNDVkNWQ4MTUwY2YxNzAwNjQ2YTViNzc0ZWJjM2UwOWM4NzMzYmIiLCJzZXNzaW9uSGFuZGxlIjoiZjNmODMzNmItNjRlMS00ZjY2LWI4YTgtZTI2YzdhYzRjMGIwIiwic3QtcGVybSI6eyJ0IjoxNzg1NDQ4MDQyLCJ2IjpbXX0sInN0LXJvbGUiOnsidCI6MTc4NTQ0ODA0MiwidiI6W119LCJzdWIiOiIyNjJiNTNmYi0zNWQwLTQzNGEtYWNjZS1jYjU1ODk5NDUyM2MiLCJ0SWQiOiJwdWJsaWMifX0=; ff=%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable_shopping_journey%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1785451642401%2C%22r%22%3A1785534442401%7D; resolution_width=955',
}

def json_builder(item):
    j = {
        'city_ids': ['1',],'data': {'form_data': {'data': {'category': {'str': {'value': item,},},},},'server_payload': {'@type': 'type.googleapis.com/widgets.SearchData.ServerPayload','additional_form_data': {'data': {'sort': {'str': {'value': 'sort_date',},},},},},},'source_view': 'CATEGORY',}
    return j


def save(fn, data, path):
    file_path = os.path.join(path, f'{fn}.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def folder_existence_checker(drname):
    try:
        for root,dirs,files in os.walk(os.getcwd()):
            if drname in dirs:
                full_path = os.path.join(root,drname)
                return full_path
        return None
    except PermissionError as e:
        print(f'{e} Permission Error on folder {drname}')

def main():
    if not os.path.exists(directory_name):
        print(f'{directory_name} Folder does not exist. Making it...')
        os.makedirs(directory_name, exist_ok=True) # این خط خطا را از بین می‌برد
    else:
        print(f'{directory_name} Folder Exists')
    with open('../categories.json', 'r', encoding='utf-8') as f:
        categories = json.load(f)
        for i in categories['category_values_to_slugs']:
            try:
                response = requests.post('https://api.divar.ir/v8/postlist/w/filters', cookies=cookies, headers=headers,json=json_builder(i))
                time.sleep(2)
                if response.status_code == 200:
                    save(i, response.json(),directory_name)
                    print(f"{i} Saved!!")
                else:
                    print(response.status_code)
                    print(f'{i} Failed!!,Continuing the program ')
                    continue
            except Exception as e:
                print(f'{e} Error Occured')
                break
            except KeyboardInterrupt as a:
                print(f"{a} Ctrl+C Pressed")
                break
            except requests.exceptions.ConnectionError as b:
                print(f"{b} Connection Error")
                break
        extract.run()

if __name__ == '__main__':
    main()
# response = requests.post('https://api.divar.ir/v8/postlist/w/filters', cookies=cookies, headers=headers, json=json_data)
# print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"city_ids":["1"],"data":{"form_data":{"data":{"category":{"str":{"value":"classic"}}}},"server_payload":{"@type":"type.googleapis.com/widgets.SearchData.ServerPayload","additional_form_data":{"data":{"sort":{"str":{"value":"sort_date"}}}}}},"source_view":"CATEGORY"}'
#response = requests.post('https://api.divar.ir/v8/postlist/w/filters', cookies=cookies, headers=headers, data=data)