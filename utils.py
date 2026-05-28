# -*- coding: utf-8 -*-

import logging
from concurrent_log import ConcurrentTimedRotatingFileHandler
import re
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

# 日志配置
logger = logging.getLogger("CTG_bot_logger")
logger.setLevel(logging.INFO)
handler = ConcurrentTimedRotatingFileHandler(
    filename="log/CTG_bot", when="MIDNIGHT", interval=1, backupCount=3, encoding="utf-8"
)
handler.suffix = "%Y-%m-%d.log"
handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


def count_token(text):
    tokens = encoding.encode(text)
    return len(tokens)
