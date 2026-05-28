# -*- coding: utf-8 -*-

# import json
import requests


def do_post(api_url, query_body_):
    response = requests.post(api_url, json=query_body_)
    print(response.text)
    # json_res = json.loads(response.text)
    # print(json_res)


query_api_url = "http://127.0.0.1:8000/encode"
query_body = {
    "texts": ["你是谁？", "你好吗？"]
}
do_post(query_api_url, query_body)
