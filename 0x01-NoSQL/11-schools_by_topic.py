#!/usr/bin/env python3
"""mongo n python"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """filters out the list of schools having a specific topic"""
    return mongo_collection.find({"topics": topic})
