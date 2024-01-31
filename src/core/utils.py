def has_intersection(query1, query2) -> bool:
    return bool(set(query1) & set(query2))
