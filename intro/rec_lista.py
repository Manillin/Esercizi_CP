def flatten(l):
    res = []
    if not hasattr(l,'__iter__'):
        return [l]
    for o in l:
        res.extend(flatten(o))
    return res


