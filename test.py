# -*- coding: utf-8 -*-

from sentence_transformers import SentenceTransformer
import time

batch_size = 128
model_path = "/apps/models/BAAI/bge-m3"
model = SentenceTransformer(model_path, device="cuda", model_kwargs={"torch_dtype": "float16"}, local_files_only=True)
print("model loaded successfully, device: {}...".format(model.device))

sentences_1 = ["That is a happy person"]
sentences_10 = ["That is a happy person"] * 10
sentences_100 = ["That is a happy person"] * 100
sentences_1000 = ["That is a happy person"] * 1000
sentences_10000 = ["That is a happy person"] * 10000

start_1 = time.time()
model.encode(sentences_1, batch_size=batch_size)
print(f"Time cost: {(time.time() - start_1) * 1000:.2f} ms")

start_10 = time.time()
model.encode(sentences_10, batch_size=batch_size)
print(f"Time cost: {(time.time() - start_10) * 1000:.2f} ms")

start_100 = time.time()
model.encode(sentences_100, batch_size=batch_size)
print(f"Time cost: {(time.time() - start_100) * 1000:.2f} ms")

start_1000 = time.time()
model.encode(sentences_1000, batch_size=batch_size)
print(f"Time cost: {(time.time() - start_1000) * 1000:.2f} ms")

start_10000 = time.time()
model.encode(sentences_10000, batch_size=batch_size)
print(f"Time cost: {(time.time() - start_10000) * 1000:.2f} ms")
