# -*- coding: utf-8 -*-

from sentence_transformers import SentenceTransformer
import time
from utils import *

batch_size = 32
model_path = "/apps/models/BAAI/bge-m3"
model = SentenceTransformer(model_path, device="cuda", local_files_only=True)
model.encode(["init model"], batch_size=batch_size)
print("Model loaded successfully, device: {}...".format(model.device))

test_text = "That is a happy person, That is a happy person, That is a happy person, That is a happy person, That is a happy person, That is a happy person"
print("Token length smaller: {}".format(count_token("That is a happy person")))
print("Token length: {}".format(count_token(test_text)))

sentences_1 = [test_text]
sentences_10 = [test_text] * 10
sentences_100 = [test_text] * 100
sentences_1000 = [test_text] * 1000
sentences_10000 = [test_text] * 10000

start_1 = time.time()
model.encode(sentences_1, batch_size=batch_size)
print(f"Time cost for 1: {(time.time() - start_1) * 1000:.2f} ms")

start_10 = time.time()
model.encode(sentences_10, batch_size=batch_size)
print(f"Time cost for 10: {(time.time() - start_10) * 1000:.2f} ms")

start_100 = time.time()
model.encode(sentences_100, batch_size=batch_size)
print(f"Time cost for 100: {(time.time() - start_100) * 1000:.2f} ms")

start_1000 = time.time()
model.encode(sentences_1000, batch_size=batch_size)
print(f"Time cost for 1000: {(time.time() - start_1000) * 1000:.2f} ms")

start_10000 = time.time()
model.encode(sentences_10000, batch_size=batch_size)
print(f"Time cost for 10000: {(time.time() - start_10000) * 1000:.2f} ms")
