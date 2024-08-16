#!/usr/bin/env python3
"""Writes a string to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Defines a class Cache"""
    def __init__(self) -> None:
        """
        Initialize a Cache instance with Redis client
        Flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
