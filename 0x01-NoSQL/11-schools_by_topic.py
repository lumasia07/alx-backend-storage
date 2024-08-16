#!/usr/bin/env python3
"""Query schools by topics"""


def schools_by_topic(mongo_collection, topic):
    """
    Query schools by topic

    Args:
        mongo_collection: pymongo collection object
        topic: strinf to be searched

    Return: list of specific schools
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
