import sys 
from collections import OrderedDict

input = sys.stdin.readline
N = int(input())
N_list = [ input().split() for _ in range(N)]
tree = OrderedDict()

for i in N_list:
    for j in range(len(i)):
        if i[j] == ".":
            i[j] = None

    if i[0] not in tree:
        tree[i[0]] = [i[1], i[2]]

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


for i in N_list:
    data, left, right = i 
    tree[data] = Node(data, left, right)

def pre_order(node):
    print(node.data, end="")
    if node.left:
        pre_order(tree[node.left])
    if node.right:
        pre_order(tree[node.right])

def in_order(node):
    if node.left:
        in_order(tree[node.left])
    print(node.data, end="")
    if node.right:
        in_order(tree[node.right])

def post_order(node):
    if node.left:
        post_order(tree[node.left])
    if node.right:
        post_order(tree[node.right])
    print(node.data, end="")

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])