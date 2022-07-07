# O(s * t)
# def subTree(root, subRoot):
#     if isMatch(root, subRoot):
#         return True
#     if not root:
#         return False
#     return subTree(root.left, subRoot) or subTree(root.right, subRoot)

# def isMatch(root, subRoot):
#     if not(root and subRoot):
#         return root is subRoot
#     return(root.val == subRoot.val and isMatch(root.left == subRoot.left) and isMatch(root.right == subRoot.right))


def isSubtree(s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()
        
    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle
        
    merkle(s)
    merkle(t)
    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or 
                dfs(node.left) or dfs(node.right))
                    
    return dfs(s)