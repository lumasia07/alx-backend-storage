#!/usr/bin/env python3
"""Writes a string to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Wrapper for count calls method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the count for the method using its qualified name"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Defines a callable method for storing """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Generate keys for inputs and outputs"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


class Cache:
    """Defines a class Cache"""
    def __init__(self) -> None:
        """
        Initialize a Cache instance with Redis client
        Flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
