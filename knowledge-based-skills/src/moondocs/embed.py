"""Local fastembed wrapper for the resolve + load passes.

BGE-small-en-v1.5 is 384-dim, ~512 token window. Used for:
  - DocChunk.embedding (HNSW vector index in FalkorDB)
  - Entity-resolution cosine similarity in resolve.py
"""
from __future__ import annotations

import os

import numpy as np
from fastembed import TextEmbedding

_EMBED_MODEL_NAME = os.environ.get("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
_model: TextEmbedding | None = None


def _get() -> TextEmbedding:
    global _model
    if _model is None:
        _model = TextEmbedding(model_name=_EMBED_MODEL_NAME)
    return _model


def embed(texts: list[str]) -> np.ndarray:
    return np.array(list(_get().embed(texts)), dtype=np.float32)
