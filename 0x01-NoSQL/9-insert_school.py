#!/usr/bin/env python3
"""mongo n python"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts new document into  the collection"""
    return mongo_collection.insert(kwargs)
