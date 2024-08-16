#!/usr/bin/env python3
"""Writes a string to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable[[bytes],
                                                  Union[str, int, bytes, float]
                                                  ]] = None) -> Optional[
                                                      Union[
                                                          str, int,
                                                          bytes, float]]:
        """Getter method for key"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Getter method for string"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Getter method for bytes"""
        return self.get(key, lambda d: int(d))
