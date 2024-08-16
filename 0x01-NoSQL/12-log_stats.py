#!/usr/bin/env python3
"""Logs nginx stats"""
from pymongo import MongoClient

def log_stats():
    """Logs Nginx stats stored in MongoDB."""
    client = MongoClient('mongodb://localhost:27017/')
    

    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_stats[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()