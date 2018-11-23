"""区间树"""
# from search import RBTree1
# 区间类
class Interval:
    def __init__(self, low=0, high=0):
        self.low = low
        self.high = high

    def __str__(self):
        return '[' + str(self.low) + ',' + str(self.high) + ']'

# 区间树类
class IntervalTree():
    def __init__(self):
        self.nil = IntervalNode(Interval(-1, -1))
        self.root = self.nil

# 区间树结点类
class IntervalNode():
    def __init__(self, interval=Interval()):
        self.interval = interval  # 区间属性
        self.key = interval.low  # 关键字存储区间的低端点
        self.color = "Black"
        self.parent = None
        self.left = None
        self.right = None
        self.max = interval.high
        # 以x为根的子树中所有区间的端点的最大值

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
    # 调整max
    x.max = max(x.interval.high, x.left.max, x.right.max)
    x.parent.max = max(x.parent.interval.high, x.max, x.parent.right.max)

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
    # 调整max
    x.max = max(x.interval.high, x.left.max, x.right.max)
    x.parent.max = max(x.parent.interval.high, x.parent.left.max, x.max)

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
    max_fixup(T, z)  # 由z结点向根调整max
    insert_fixup(T, z)

# max调整
def max_fixup(T, z):
    temp = z
    while temp != T.nil:
        temp.max = max(temp.interval.high, temp.left.max, temp.right.max)
        temp = temp.parent

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

# 判断区间是否重叠
def overlap(self, i):
    if self.low <= i.high and i.low <= self.high:
        return True
    else:
        return False

# 查找区间
def interval_search(T, i):
    x = T.root
    while x != T.nil and overlap(x.interval, i) == False:
        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return x

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
def minimum(T, x):
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
        if x.key != -1:
            print('interval:', x.interval, '\tkey:', x.key,
                  '\tmax:', x.max, '\tcolor:', x.color)
        pre_order(x.left)
        pre_order(x.right)

# 中序遍历
def mid_order(x):
    if x != None:
        mid_order(x.left)
        if x.key != -1:
            print('interval:', x.interval, '\tkey:', x.key,
                  '\tmax:', x.max, '\tcolor:', x.color)
        mid_order(x.right)

# 后序遍历
def post_order(x):
    if x != None:
        post_order(x.left)
        post_order(x.right)
        if x.key != -1:
            print('interval:', x.interval, '\tkey:', x.key,
                  '\tmax:', x.max, '\tcolor:', x.color)

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
    T = IntervalTree()
    nodes = [Interval(16, 21), Interval(8, 9), Interval(25, 30),
             Interval(5, 8), Interval(15, 23), Interval(17, 19),
             Interval(26, 26), Interval(0, 3), Interval(6, 10),
             Interval(19, 20)]
    for node in nodes:
        insert_node(T, IntervalNode(node))

    print_tree(T.root)

    result = interval_search(T, Interval(10, 12))
    print("查找区间[10, 12]")
    if result == T.nil:
        print('未找到重叠区间')
    else:
        print('找到重叠区间')
        print('interval:', result.interval, '\tkey:', result.key,
              '\tmax:', result.max, '\tcolor:', result.color)

    result = interval_search(T, Interval(11, 14))
    print("查找区间[11, 14]")
    if result == T.nil:
        print('未找到重叠区间')
    else:
        print('找到重叠区间')
        print('interval:', result.interval, '\tkey:', result.key,
              '\tmax:', result.max, '\tcolor:', result.color)