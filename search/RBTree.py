"""红黑树"""
# 红黑树类
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

# 红黑树结点类
class RBTreeNode(object):
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'

# 左旋
def left_rotate(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

# 右旋
def right_rotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

# 插入结点
def insert_node(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil  # 初始化节点
    z.right = T.nil
    z.color = 'red'
    insert_fixup(T, z)

# 插入调整
def insert_fixup(T, z):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'red':  # case 1
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:  # case 2
                    z = z.parent
                    left_rotate(T, z)
                z.parent.color = 'black'  # case 3
                z.parent.parent.color = 'red'
                right_rotate(T, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    right_rotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                left_rotate(T, z.parent.parent)
    T.root.color = 'black'

# 替换结点
def transplant(T, u, v):
    if u.parent == T.nil:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent

# 寻找后继
def minimum(x):
    while x.left != T.nil:
        x = x.left
    return x

# 删除节点
def delete_node(T, z):
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        transplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        transplant(T, z, z.left)
    else:
        y = minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color
    if y_original_color == 'black':
        RBDeleteFixup(T, x)

# 删除调整
def RBDeleteFixup(T, x):
    while x != T.root and x.color == 'black':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                left_rotate(T, x.parent)
                w = x.parent.right
            if w.left.color == 'black' and w.right.color == 'black':
                w.color = 'red'
                x = x.parent
            else:
                if w.right.color == 'black':
                    w.left.color = 'black'
                    w.color = 'red'
                    right_rotate(T, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 'black'
                w.right.color = 'black'
                left_rotate(T, x.parent)
                x = T.root
        else:
            w = x.parent.left
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                right_rotate(T, x.parent)
                w = x.parent.left
            if w.right.color == 'black' and w.left.color == 'black':
                w.color = 'red'
                x = x.parent
            else:
                if w.left.color == 'black':
                    w.right.color = 'black'
                    w.color = 'red'
                    left_rotate(T, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 'black'
                w.left.color = 'black'
                right_rotate(T, x.parent)
                x = T.root
    x.color = 'black'

# 先序遍历
def pre_order(x):
    if x != None:
        if x.key != 0:
            print('key:', x.key, '\tx.color:', x.color)
        pre_order(x.left)
        pre_order(x.right)

# 中序遍历
def mid_order(x):
    if x != None:
        mid_order(x.left)
        if x.key != 0:
            print('key:', x.key, '\tx.color:', x.color)
        mid_order(x.right)

# 后序遍历
def post_order(x):
    if x != None:
        post_order(x.left)
        post_order(x.right)
        if x.key != 0:
            print('key:', x.key, '\tx.color:', x.color)

# 打印树的三种遍历
def print_tree(x):
    print("先序遍历结果：")
    pre_order(x)
    print()
    print("中序遍历结果：")
    mid_order(x)
    print()
    print("后序遍历结果：")
    post_order(x)
    print()

if __name__ == "__main__":
    nodes = [41, 38, 31, 12, 19, 8]
    T = RBTree()
    for node in nodes:
        insert_node(T, RBTreeNode(node))
    print_tree(T.root)
    delete_node(T, T.root)
    print_tree(T.root)