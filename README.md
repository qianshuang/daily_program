# 一、Tips

1. 生成requirements.txt：pipreqs --force ./
2. restart
   1. ps aux | grep python 
   2. kill -9 -主进程号 举例：kill -9 -1265
   3. nohup uvicorn main:app --workers 4 --host 0.0.0.0 & 

# 二、接口描述

| 请求URL | https://127.0.0.1:8001/encode                                                          |
|-------|----------------------------------------------------------------------------------------|
| 请求方式  | POST                                                                                   |
| 请求体   | {'query': 'User: what is your name?', 'history': ['User: hello', 'AI: Hello']}         |
| 返回值   | 成功：{'code': 0, 'msg': 'success', 'data': 'reply'}<br/>失败：{'code': -1, 'msg': 'failed'} |
| 接口说明  |                                                                                        |