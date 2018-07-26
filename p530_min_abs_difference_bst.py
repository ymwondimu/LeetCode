def get_min(root):
    min_val = float('inf')
    res = []
    in_order(root, res)
    for i in range(1, len(res)):
        min_val = min(min_val, abs(res[i] - res[i-1]))

    return min_val

def in_order(root, res):
    if root:
        in_order(root.left)
        res.append(root.value)
        in_order(root.right)