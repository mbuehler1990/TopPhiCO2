
def rowsCols(a):
    if len(a.shape) > 1:
        rows = a.shape[0]
        cols = a.shape[1]
    else:
        rows = a.shape[0]
        cols = 0
    return rows, cols
