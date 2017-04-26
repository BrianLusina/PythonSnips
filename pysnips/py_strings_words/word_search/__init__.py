def word_search(query, seq):
    return [x for x in seq if query.lower() in x.lower()] or [str(None)]
