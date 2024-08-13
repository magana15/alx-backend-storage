#!/usr/bin/env python3
"""All students sorted by their average score"""


def top_students(mongo_collection):
    """return all students sorted by ave score"""
    top_stds = mongo_collection.aggregate([
            {
                "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
        ])
    return top_stds
