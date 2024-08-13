#!/usr/bin/env python3
"""Insert with args"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new doc in collection

    Params:
    mongo_collection: collection object
    **kwargs: key-value pair for field-values

    Returns:
    ObjectId: _id of newly inserted object
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
