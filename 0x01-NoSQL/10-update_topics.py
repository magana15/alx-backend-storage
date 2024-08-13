#!/usr/bin/env python3
"""mongo n python"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """updates all the topics of the school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
