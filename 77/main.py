output = []

def combine(n, k):
    helper([], 0, n ,k)
    return output

def helper(cur, index, n, remainding):

    # print(cur, index, n ,remainding)
    
    if remainding <= 0:
        output.append(cur)
        return

    if index >= n:
        return

    # include
    new_cur = cur.copy()
    new_cur.append(index + 1)
    helper(new_cur, index + 1, n, remainding - 1)

    # don't include
    helper(cur, index + 1, n, remainding)

print(combine(5, 3))


