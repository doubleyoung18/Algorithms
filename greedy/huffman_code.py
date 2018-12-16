#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@Author:Double Young
@Time:2018/12/11 14:49:13
@Desc:哈夫曼编码(贪心)
"""

class Node:
    def __init__(self, char=None, freq=0):
        """
        结点类
        :param char: 字符
        :param freq: 频数
        """
        self.char = char # 字符
        self.freq = freq  # 频数
        self.left = None
        self.right = None

def create_huffman_tree(freq_dist):
    """
    创建哈夫曼树-O(nlgn)
    :param node_list: 结点队列
    :return: 树，根
    """
    # 1.按频数快排
    freq_list = sorted(freq_dist.items(), key=lambda item: item[1])
    node_list = [Node(item[0], item[1]) for item in freq_list]  # 结点列表
    queue = node_list[:]  # 结点队列
    node_root = None
    while len(queue) > 1:
        # 2.取两个头结点
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        # 3.合并成新结点
        node_root = Node(None, node_left.freq+node_right.freq)
        # 4.新旧结点连接
        node_root.left = node_left
        node_root.right = node_right
        # 5.新结点按序插入队列
        for i in range(len(queue)):
            if node_root.freq < queue[i].freq:
                queue = queue[:i] + [node_root] + queue[i:]
                break
            else:  # 若遍历至队尾
                if i == len(queue)-1:
                    queue.append(node_root)
    return node_list, node_root

def generate_code(root, code_dist, code):
    """
    生成哈夫曼编码(先序遍历)-O(n)
    :param root: 根
    :param code_dist: 编码字典
    :param code: 当前编码
    :return: 编码字典
    """
    if root != None:
        if root.char != None:
            code_dist[root.char] = code
        generate_code(root.left, code_dist, code+"1")
        generate_code(root.right, code_dist, code+"0")
    return code_dist

def huffman_encode(src, code_dist):
    """
    哈夫曼编码-O(n)
    :param src: 编码前字符串
    :param code_dist: 编码字典
    :return: 编码后字符串
    """
    dest = ""
    for ch in src:
        dest += code_dist[ch]
    return dest

def huffman_decode(src, root):
    """
    哈夫曼解码-O(nlgn)
    :param src: 解码前字符串
    :param code_dist: 哈夫曼树根
    :return: 解码后字符串
    """
    dest = ""
    node = root
    for ch in src:
        if node.left == None:  # 若 当前结点为叶子
            dest += node.char
            node = root  # 从根重新搜索
        if ch == "1":
            node = node.left
        if ch == "0":
            node = node.right
    dest += node.char  # 最后一个字符解码
    return dest

def cal_freqs(string):
    """
    计算字符频度-O(n^2)
    :param string: 输入字符串
    :return: 频度字典
    """
    freq_dist = {}
    for ch in string:
        if ch != None and ch not in freq_dist.keys():
            freq_dist[ch] = string.count(ch, 0, len(string))
    return freq_dist

if __name__ == "__main__":
    # string_input = "hello world"
    string_input = input("输入编码字符串：")
    freq_dist = cal_freqs(string_input)
    print("字符频数统计字典：")
    for item in freq_dist.items():
        print(item)

    print("--------------------")
    print("哈夫曼编码字典：")
    node_list, root = create_huffman_tree(freq_dist)
    code_dist = generate_code(root, {}, "")
    for item in code_dist.items():
        print(item)

    print("--------------------")
    print("哈夫曼编码结果：")
    string_encode = huffman_encode(string_input, code_dist)
    print(string_encode)

    print("--------------------")
    print("哈夫曼解码结果：")
    string_decode = huffman_decode(string_encode, root)
    print(string_decode)