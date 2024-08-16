#!/usr/bin/env python3
"""Caching"""
import requests
import redis
from functools import wraps
from typing import Callable

redis_client = redis.Redis()


def cache_page(expiration: int = 10) -> Callable:
    """Decorator to cache the result of get_page."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            redis_client.incr(f"count:{url}")
            cached_page = redis_client.get(f"cache:{url}")
            if cached_page:
                return cached_page.decode('utf-8')
            page_content = func(url)
            redis_client.setex(f"cache:{url}", expiration, page_content)
            return page_content
        return wrapper
    return decorator


@cache_page(expiration=10)
def get_page(url: str) -> str:
    """Fetch the content of URL and return content."""
    response = requests.get(url)
    return response.text
