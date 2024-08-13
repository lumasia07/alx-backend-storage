#!/usr/bin/env python3
"""List all docs in python"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all docs in mongo collection

    Args:
    mongo_collection: MongoCollection object

    Returns:
    list: A list of dictionaries
    """
    return list(mongo_collection.find())
