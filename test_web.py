# -*- coding: utf-8 -*-

# import json
import requests
from utils import *


def do_post(api_url, query_body_):
    response = requests.post(api_url, json=query_body_)
    print(response.text)
    # json_res = json.loads(response.text)
    # print(json_res)


query_api_url = "http://127.0.0.1:8888/encode"
query_body = {
    "texts": ["""你好吗？""", """我很好。"""]
}
# print(count_token(query_body["texts"][0]))
do_post(query_api_url, query_body)
