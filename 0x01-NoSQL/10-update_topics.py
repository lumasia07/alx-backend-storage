#!/usr/bin/env python3
"""Update topics"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics of docs in collection
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
