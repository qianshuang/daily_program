# -*- coding: utf-8 -*-

import os
from typing import cast
import numpy as np
from pydantic import BaseModel, Field
from fastapi import FastAPI
from utils import *
from sentence_transformers import SentenceTransformer
import time

batch_size = 128
model_path = "/apps/models/BAAI/bge-m3"
model = SentenceTransformer(model_path, device="cuda", model_kwargs={"torch_dtype": "float16"}, local_files_only=True)
print(model.device)


class EmbeddingBody(BaseModel):
    texts: list = Field(default_factory=list)


app = FastAPI()


@app.post("/encode")
async def encode(eb: EmbeddingBody):
    print("{} is processing...".format(os.getpid()))
    try:
        start = time.time()
        result = cast(np.ndarray, model.encode(eb.texts, batch_size=batch_size))
        print(f"Time cost: {(time.time() - start) * 1000:.2f} ms")
        return {"code": 0, "msg": "success", "data": result.tolist()}
    except Exception as e:
        logger.exception(f"call encode failed: {e}......")
        return {'code': -1, 'msg': "call encode failed......"}
