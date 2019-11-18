def inorder(head):
    stack = []
    res = []
    p = head

    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            top = stack.pop()
            res.append(top.val)
            p = top.right

    return res


def preorder(head):
    stack = []
    res = []
    p = root

    while p or stack:
        if p:
            stack.append(p)
            res.append(p.val)
            p = p.left
        else:
            top = stack.pop()
            p = top.right
    return res

def postorder(head):
    stack = []
    res = []
    p = root
    while p or stack:
    if p:
        stack.append(p)
        res.insert(0, p.val)
        p = p.right
    else:
        top = stack.pop()
        p = top.left
    return res
