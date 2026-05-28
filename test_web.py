# -*- coding: utf-8 -*-

# import json
import requests


def do_post(api_url, query_body_):
    response = requests.post(api_url, json=query_body_)
    print(response.text)
    # json_res = json.loads(response.text)
    # print(json_res)


query_api_url = "http://127.0.0.1:8000/chat"
query_body = {
    "query": "对公付款申请，收款方银行怎么搜不到？",
    "history": [{"type": "human", "data": "aaaaaaaaa"}]
}
do_post(query_api_url, query_body)
