import sys 
from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())
islands = [ input().split() for _ in range(M)]
locations = input().split()


def bfs(v):
    visited = [False] * N
    queue = deque([v])
